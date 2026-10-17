TARGET_PORT="8000"
LOG_FILE="network_answer.log"

echo "=== CHECKING FOR ANSWER ==="

PORT_CHECK=$(sudo netstat -tulnp | grep ":$TARGET_PORT " | grep "LISTEN")

if [ -n "$PORT_CHECK" ]; then
    echo "[$(date)] Succes: Port $TARGET_PORT listening." >> $LOG_FILE
    echo "Port: $TARGET_PORT works very well."
else
    echo "[$(date)] Critical error: Port $TARGET_PORT CLOSED! server is down!" >> $LOG_FILE
    echo "WARNING! Port $TARGET_PORT is ignoring!"
fi

echo "Log Succesfully saved in $LOG_FILE"