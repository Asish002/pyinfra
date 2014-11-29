# pyinfra
# File: pyinfra/__init__.py
# Desc: some global state for pyinfra

import logging

# Global logger
logger = logging.getLogger('pyinfra')

# Internal connections
_connections = {}

# Current server host
_current_server = None

# Data for all hosts/servers
_commands = {}
_facts = {}
_meta = {}
_results = {}