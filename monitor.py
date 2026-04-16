from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer

log = core.getLogger()

prev_bytes = {}

def _handle_ConnectionUp(event):
    log.info("Switch %s connected. Starting Monitor...", event.connection)

    # Request flow statistics every 5 seconds
    Timer(5, request_stats, recurring=True, args=[event.connection])

def request_stats(connection):
    connection.send(
        of.ofp_stats_request(
            body=of.ofp_flow_stats_request()
        )
    )

def _handle_FlowStatsReceived(event):
    global prev_bytes

    for stat in event.stats:
        key = (stat.match.in_port, stat.match.dl_dst)
        current_bytes = stat.byte_count

        if key in prev_bytes:
            diff = current_bytes - prev_bytes[key]

            # Ignore negative values caused by counter resets or flow expiry
            if diff < 0:
                diff = 0

            # Bandwidth = Delta Bytes / Time Interval
            bw = diff / 5.0

            log.info(
                "Port %s -> Dest %s | Utilization: %.2f Bytes/sec",
                stat.match.in_port,
                stat.match.dl_dst,
                bw
            )

        prev_bytes[key] = current_bytes

def launch():
    core.openflow.addListenerByName(
        "ConnectionUp",
        _handle_ConnectionUp
    )

    core.openflow.addListenerByName(
        "FlowStatsReceived",
        _handle_FlowStatsReceived
    )

