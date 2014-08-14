

#validation DS
server_fields = {
    "match_keys": "['id', 'mac_address', 'cluster_id', 'ip_address', 'tag']",
    "obj_name": "server",
    "primary_keys": "['id', 'mac_address']",
    "id": "",
    "host_name": "",
    "mac_address": "",
    "ip_address": "",
    "parameters": """{
                    'interface_name': ''
                    }""",
    "roles": ["config","openstack","control","compute","collector","webui","database"],
    "cluster_id": "",
    "subnet_mask": "",
    "gateway": "",
    "password": "",
    "domain": "",
    "email": "",
    "power_username": "",
    "power_type": "",
    "power_password": "",
    "control_data_network": "",
    "bond_interface": "",
    "power_address": "",
    "tag": ""
}

cluster_fields = {
    "match_keys": "['id']",
    "obj_name": "cluster",
    "id": "",
    "email": "",
    "primary_keys": "['id']",
    "parameters": """{
                'router_asn': '64512',
                'database_dir': '/home/cassandra',
                'database_token': '',
                'openstack_mgmt_ip': '',
                'use_certificates': 'False',
                'multi_tenancy': 'False',
                'encapsulation_priority': 'MPLSoUDP,MPLSoGRE,VXLAN',
                'service_token': 'contrail123',
                'keystone_username': 'admin',
                'keystone_password': 'contrail123',
                'keystone_tenant': 'admin',
                'openstack_passwd': 'contrail123',
                'analytics_data_ttl': '168',
                'haproxy': 'disable',
                'subnet_mask': '255.255.255.0',
                'gateway': '10.204.221.46',
                'password': 'c0ntrail123',
                'external_bgp': '',
                'domain': 'contrail.juniper.net'
                }"""
}

image_fields = {
    "match_keys": "['id']",
    "obj_name": "image",
    "primary_keys": "['id']",
    "id": "",
    "type": "",
    "version": "",
    "path": ""
}

