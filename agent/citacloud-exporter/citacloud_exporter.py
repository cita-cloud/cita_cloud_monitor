#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This is the exporter script for the CITA Cloud Monitor monitoring system.
The data on the chain is obtained via gRPC and then pulled by prometheus.
"""

# pylint: disable=global-statement, too-many-locals, too-many-branches, too-many-statements, fixme, import-error, line-too-long 
# TODO: refactor codes to pass pylint

import json, base64
import os
import sys
import time
import platform
import prometheus_client
import toml
from prometheus_client.core import CollectorRegistry, Gauge
from flask import Response, Flask
import argparse
import coloredlogs, logging

# grpc
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/grpcstub")
import grpc
from grpc import _grpcio_metadata
import common_pb2 as common
import controller_pb2 as CitaCloudController
import controller_pb2_grpc as CitaCloudControllerGrpc
from google.protobuf.json_format import MessageToJson

# logging
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

# exporter value variable
NODE_FLASK        = Flask(__name__)
EXPORTER_HOST     = None
EXPORTER_PORT     = None
GRPC_HOST         = None
GRPC_PORT         = None
GRPC_VERSION      = _grpcio_metadata.__version__
NODE_DATA_FOLDER  = None
EXPORTER_PLATFORM = platform.platform()
AGENT_NAME        = platform.node()

# exporter label variable
SERVICE_STATUS_TITLE = "[ value is 1 or 0 ] \
Check the running status of the CITA service, service up is 1 or down is 0."

GENESIS_BLOCK_DETAILS_TITLE = "[ value is genesis block timestamp ] \
Get information about the genesis block."

CHAIN_INFO_TITLE = "[ value is 1 or 0 ] \
Get the basic information of the chain, the economic model Quota is 0 or Charge is 1."

NODE_PEERS_TITLE = "[ value is local node peer count ] \
Get the number of peers connected to the local node."

CHAIN_NODES_TITLE = "[ value is node count of chain ] \
Get the number of consensus nodes on the chain."

LAST_BLOCK_NUMBER_TITLE = "[ value is last block number ] \
Get the latest block height."

CHECK_PROPOSER_TITLE = "[ value is 1 or 0 ] \
Check the local node address is proposal, proposal is 1 or listeners is 0."

LAST_BLOCK_DETAILS_TITLE = "[ value is last block timestamp ] \
Get the latest block details."

BLOCK_HEIGHT_DIFFERENCE_TITLE = "[ value is interval ] \
Get current block time and previous block time, label include CurrentHeight, PreviousHeight."

BLOCK_INTERVAL_TITLE = "[ value is interval ] \
Get current block time and previous block time."

LAST_BLOCK_TRANSACTIONS_TITLE = "[ value is tx counts ] \
Get the number of transactions in the current block."

LAST_BLOCK_QUOTA_USED_TITLE = "[ value is quotaused of block ] \
Get quotaused in current block."

CHAIN_QUOTA_PRICE_TITLE = "[ value is quota price ] \
Get Quota price of chain."

BLOCK_QUOTA_LIMIT_TITLE = "[ value is block quota limit ] \
Get block quota limit of chain."

VOTE_NODE_TITLE = "[ value is confirm vote ] \
Get vote list of current block."

LOCAL_VOTE_TITLE = "[ value is local is voter ] \
Determine if the local node address is in the voter list."

BLOCK_VOTE_NUMBER_TITLE = "[ value is block vote number ] \
Number of nodes voted by the statistics block."

# class
class GrpcWrapper():
    """This class is to get CITA data"""

    def __init__(self, grpc_host, grpc_port):
        self.grpc_host = grpc_host
        self.grpc_port = grpc_port
        # initialize grpc
        channel = grpc.insecure_channel('%s:%s' % (self.grpc_host, self.grpc_port))
        self.grpc_stub = CitaCloudControllerGrpc.RPCServiceStub(channel)

    def cli_request(self, service_name, payload):
        """Cita-cli request method"""
        log_time = time.asctime(time.localtime(time.time()))
        try:
            message = getattr(self.grpc_stub, service_name)(payload)
            json_string = MessageToJson(message, including_default_value_fields=True)
        except:
            result = "%s - Error - exec error[ %s ]\n" % (log_time, service_name)
        else:
            result = json.loads(json_string)
        logger.debug("Service Name: %s, Parameter: %s, Result: %s" % (service_name, payload, result))
        return result

    def metadata(self):
        """Get metadate"""
        return self.cli_request("GetSystemConfig", common.Empty())

    def block_number(self):
        """Get the current block height"""
        return self.cli_request("GetBlockNumber", CitaCloudController.Flag(flag=True))

    def GetBlockByNumber(self, block_number_int):
        """Get detailed information about CITA blocks with cita-cli"""
        return self.cli_request("GetBlockByNumber", CitaCloudController.BlockNumber(block_number=block_number_int))

    def quota_price(self):
        """Get CITA quota price"""
        raise NotImplementedError("scm PriceManager getQuotaPrice not implemented.")

    def block_limit(self):
        """Get the quota limit for cita blocks"""
        raise NotImplementedError("scm QuotaManager getBQL not implemented.")

    def get_node_address(self):
        """Get the Node Address"""
        with open("%s/config.toml" % (NODE_DATA_FOLDER)) as config_file:
            res = toml.load(config_file)
            return res['controller']['node_address']


# flask object
@NODE_FLASK.route("/metrics")
def metrics():
    """Agent execution function"""

    # tags definition
    registry = CollectorRegistry(auto_describe=False)
    service_status = Gauge("Node_Get_ServiceStatus", SERVICE_STATUS_TITLE, ["NodeIP", "NodePort"], registry=registry)
    genesis_block_details = Gauge("Node_Get_GenesisBlockNumberDetails", GENESIS_BLOCK_DETAILS_TITLE, ["NodeIP", "NodePort", "GenesisBlockNumberHash"], registry=registry)
    chain_info = Gauge("Node_Get_ChainInfo", CHAIN_INFO_TITLE,
                       ["NodeIP", "NodePort", "ChainName", "Operator", "TokenName", "TokenSymbol", "Version"], registry=registry)
    node_peers = Gauge("Node_Get_NodePeers", NODE_PEERS_TITLE,
                       ["NodeIP", "NodePort"], registry=registry)
    chain_nodes = Gauge("Node_Get_ChainNodes", CHAIN_NODES_TITLE,
                        ["NodeIP", "NodePort"], registry=registry)
    last_block_number = Gauge("Node_Get_LastBlockNumber", LAST_BLOCK_NUMBER_TITLE,
                              ["NodeIP", "NodePort", "GenesisBlockNumberHash", "NodeID", "NodeAddress"], registry=registry)
    check_proposer = Gauge("Node_CheckProposer", CHECK_PROPOSER_TITLE, ["NodeIP", "NodePort"], registry=registry)
    last_block_details = Gauge("Node_Get_LastBlockNumberDetails", LAST_BLOCK_DETAILS_TITLE,
                               ["NodeIP", "NodePort", "LastBlocknumber", "LastBlockProposer", "LastBlockHash", "NodeID",
                                   "HostPlatform", "HostName", "ConsensusStatus", "SoftVersion"], registry=registry)
    vote_node = Gauge("Node_Get_VoteNode", VOTE_NODE_TITLE,
                      ["NodeIP", "NodePort", "NodeID", "Voter"], registry=registry)
    block_height_difference = Gauge("Node_Get_BlockDifference", BLOCK_HEIGHT_DIFFERENCE_TITLE,
                                    ["NodeIP", "NodePort", "CurrentHeight", "PreviousHeight"], registry=registry)
    block_interval = Gauge("Node_Get_BlockTimeDifference", BLOCK_INTERVAL_TITLE, ["NodeIP", "NodePort"], registry=registry)
    last_block_transactions = Gauge("Node_Get_LastBlockNumberTransactions", LAST_BLOCK_TRANSACTIONS_TITLE, ["NodeIP", "NodePort"], registry=registry)
    last_block_quota_used = Gauge("Node_Get_LastBlockNumberQuotaUsed", LAST_BLOCK_QUOTA_USED_TITLE, ["NodeIP", "NodePort"], registry=registry)
    chain_quota_price = Gauge("Node_Get_QuotaPrice", CHAIN_QUOTA_PRICE_TITLE, ["NodeIP", "NodePort"], registry=registry)
    block_quota_limit = Gauge("Node_Get_BlockQuotaLimit", BLOCK_QUOTA_LIMIT_TITLE, ["NodeIP", "NodePort"], registry=registry)
    local_voter = Gauge("Node_Get_LocalVoter", LOCAL_VOTE_TITLE, ["NodeIP", "NodePort"], registry=registry)
    vote_number = Gauge("Block_Vote_Number", BLOCK_VOTE_NUMBER_TITLE, ["NodeIP", "NodePort"], registry=registry)

    # run exporter
    grpc_wrapper = GrpcWrapper(GRPC_HOST, GRPC_PORT)
    node_address = grpc_wrapper.get_node_address()
    logger.debug("Node Address: %s" % (node_address))

    ## Exporter Status
    service_status.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT).set(1)

    ## Genesis Block
    genesis_block_info = grpc_wrapper.GetBlockByNumber(0)
    genesis_block_hash = base64.b64decode(genesis_block_info['header']['prevhash']).hex()
    genesis_block_time = genesis_block_info['header']['timestamp']
    genesis_block_details.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT, GenesisBlockNumberHash=genesis_block_hash).set(genesis_block_time)
    logger.debug("Genesis Block - Hash: %s, Time: %s" % (genesis_block_hash, genesis_block_time))

    ## Last Block
    block_number_info = grpc_wrapper.block_number()
    last_block_number_int = int(block_number_info["blockNumber"])
    prev_block_number_int = last_block_number_int - 1
    last_block_number.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT, NodeID=node_address, GenesisBlockNumberHash=genesis_block_hash, NodeAddress=node_address).set(last_block_number_int)
    logger.debug("Block Number - Last: %s, Previous: %s" % (last_block_number_int, prev_block_number_int))

    ## Metadata
    metadata_info = grpc_wrapper.metadata()
    chain_name = None  # TODO metadata_info['chainName']
    operator = None  # TODO metadata_info['operator']
    token_name = None  # TODO metadata_info['tokenName']
    token_symbol = None  # TODO metadata_info['tokenSymbol']
    economical_model = 0  # TODO metadata_info['economicalModel']
    chain_version = metadata_info['version']
    chain_info.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT, ChainName=chain_name,
                      Operator=operator, TokenName=token_name, TokenSymbol=token_symbol,
                      Version=chain_version).set(economical_model)

    ## Chain Nodes
    consensus_node_list = [ base64.b64decode(validator).hex() for validator in metadata_info['validators']]
    consensus_node_count = len(consensus_node_list)
    chain_nodes.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT).set(consensus_node_count)

    ##
    block_info = grpc_wrapper.GetBlockByNumber(last_block_number_int)
    previous_block_info = grpc_wrapper.GetBlockByNumber(prev_block_number_int)
    block_head_info = block_info['header']
    block_commits = [] # TODO list(block_info['header']['proof']['Bft']['commits'].keys())
    consensus_nodes_count = len(consensus_node_list)
    for i in range(consensus_nodes_count):
        voter_address = consensus_node_list[i]
        vote_status = 1 if voter_address in block_commits else 0
        vote_node.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT, NodeID=node_address, Voter=voter_address).set(vote_status)
    is_committer = 1 if node_address in block_commits else 0
    local_voter.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT).set(is_committer)

    block_vote_number = len(block_commits)
    vote_number.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT).set(block_vote_number)
    logger.debug("Vote Number - block_vote_number: %s " % (block_vote_number))

    last_block_hash_base64 = grpc_wrapper.cli_request("GetBlockHash", CitaCloudController.BlockNumber(block_number=last_block_number_int))['hash']
    last_block_hash = base64.b64decode(last_block_hash_base64).hex()
    block_time = int(block_head_info['timestamp'])
    block_proposer = base64.b64decode(block_head_info['proposer']).hex()
    previous_block_time = int(previous_block_info['header']['timestamp'])
    consensus = 1 if node_address in consensus_node_list else 0
    node_software_version=grpc_wrapper.cli_request("GetVersion", common.Empty())["version"]
    last_block_details.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT, NodeID=node_address,
                              LastBlocknumber=last_block_number_int, LastBlockProposer=block_proposer,
                              LastBlockHash=last_block_hash, HostPlatform=EXPORTER_PLATFORM, HostName=AGENT_NAME,
                              ConsensusStatus=consensus, SoftVersion=node_software_version).set(block_time)
    logger.debug("Last Block Details - Last Block Hash: %s " % (last_block_hash))

    interval = abs(block_time - previous_block_time)
    block_height_difference.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT, CurrentHeight=last_block_number_int, PreviousHeight=prev_block_number_int).set(interval)
    block_interval.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT).set(interval)

    ## Last Block Transactions
    block_transactions = len(block_info.get('body').get('txHashes'))
    last_block_transactions.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT).set(block_transactions)

    ## Last Block Quota Used
    if block_head_info.get('quotaUsed'):
        block_quota_used = int(block_head_info['quotaUsed'], 16)
    else:
        block_quota_used = 0 # TODO int(block_head_info['gasUsed'], 16)  #Get the previous version of CITA v0.19.1 gasUsed    
    last_block_quota_used.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT).set(block_quota_used)

    ## Check Proposer
    proposer = 1 if node_address == block_proposer else 0
    check_proposer.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT).set(proposer)
    logger.debug("CheckProposer - Node Address: %s, Block Proposer: %s" % (node_address, block_proposer))

    # Peer Info
    peer_count = grpc_wrapper.cli_request("GetPeerCount", common.Empty())["peerCount"]
    node_peers.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT).set(peer_count)

    ## Quota Price
    # quota_price = grpc_wrapper.quota_price()
    # price = quota_price
    # chain_quota_price.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT).set(int(price, 16))

    ## Block Limit
    # block_limit = grpc_wrapper.block_limit()
    # limit = block_limit
    # block_quota_limit.labels(NodeIP=GRPC_HOST, NodePort=GRPC_PORT).set(int(limit, 16))

    # Response
    return Response(prometheus_client.generate_latest(registry), mimetype="text/plain")


# flask object
@NODE_FLASK.route("/")
def index():
    """Page data view entry"""
    body = """
<html>
    <head><title>CITA Cloud Exporter</title></head>
    <body><h1>CITA Cloud Exporter</h1><p><a href="/metrics">Metrics</a></p></body>
</html>"""
    return body

# main
if __name__ == "__main__":

    # parse command line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument("--exporter-host", default="0.0.0.0", help="Exporter listen address")
    parser.add_argument("--exporter-port", default="9349", help="Exporter listen port")
    parser.add_argument("--node-grpc-host", required=True, help="CITA Cloud Node gRPC host")
    parser.add_argument("--node-grpc-port", required=True, help="CITA Cloud Node gRPC port")
    parser.add_argument("--node-data-folder", required=True, help="CITA Cloud Node Data Folder")
    args = parser.parse_args()

    # initialize global params
    EXPORTER_HOST = args.exporter_host
    EXPORTER_PORT = args.exporter_port
    GRPC_HOST = args.node_grpc_host
    GRPC_PORT = args.node_grpc_port
    NODE_DATA_FOLDER = args.node_data_folder

    # start the exporter
    NODE_FLASK.run(host=EXPORTER_HOST, port=EXPORTER_PORT)

