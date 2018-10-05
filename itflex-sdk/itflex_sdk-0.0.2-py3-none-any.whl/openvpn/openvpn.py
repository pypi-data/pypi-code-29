from itflex_sdk.common import SdkBase
from itflex_sdk.openvpn.ca import (
    create_ca,
    delete_ca,
    get_ca,
    get_cas_pages,
    update_ca,
)
from itflex_sdk.openvpn.client_s2s import (
    create_client_site2site,
    get_client_site2site,
    get_client_site2site_config,
    get_client_site2site_configs_pages,
    get_clients_site2site_pages,
    revoke_client_site2site,
    update_client_site2site,
    update_client_site2site_config,
)
from itflex_sdk.openvpn.client_s2u import (
    create_client_site2user,
    get_client_site2user,
    get_clients_site2user_pages,
    revoke_client_site2user,
    update_client_site2user,
)
from itflex_sdk.openvpn.instance import (
    create_instance,
    delete_instance,
    get_instance,
    get_instances_pages,
    reload_instance,
    update_instance,
)
from itflex_sdk.openvpn.instance_model import (
    create_instance_model,
    delete_instance_model,
    get_default_instance_model,
    get_instance_model,
    get_instances_models_pages,
    update_instance_model,
)


class Openvpn(SdkBase):
    methods = [
        create_ca,
        delete_ca,
        get_ca,
        get_cas_pages,
        update_ca,
        create_client_site2user,
        get_client_site2user,
        get_clients_site2user_pages,
        revoke_client_site2user,
        update_client_site2user,
        create_instance_model,
        delete_instance_model,
        get_default_instance_model,
        get_instance_model,
        get_instances_models_pages,
        update_instance_model,
        create_instance,
        delete_instance,
        get_instance,
        get_instances_pages,
        reload_instance,
        update_instance,
        create_client_site2site,
        update_client_site2site,
        get_clients_site2site_pages,
        get_client_site2site,
        revoke_client_site2site,
        update_client_site2site_config,
        get_client_site2site_config,
        get_client_site2site_configs_pages,
    ]
