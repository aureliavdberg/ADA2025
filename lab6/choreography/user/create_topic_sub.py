import logging

from user_consumer import create_subscription
from user_publisher import create_topic

logging.getLogger().setLevel(logging.INFO)
create_topic("mythical-lens-450121-n0", "order_req")
create_subscription("mythical-lens-450121-n0", "order_req", "order_req_sub")
create_topic("mythical-lens-450121-n0", "inventory_status")
create_topic("mythical-lens-450121-n0", "order_status")
create_topic("mythical-lens-450121-n0", "order_status_user")
create_subscription("mythical-lens-450121-n0", "order_status_user", "order_status_user_sub")
create_topic("mythical-lens-450121-n0", "order_req")
create_topic("mythical-lens-450121-n0", "inventory_status")
create_subscription("mythical-lens-450121-n0", "inventory_status",
                    "inventory_status_sub")
create_subscription("mythical-lens-450121-n0", "order_status","order_status_sub")
