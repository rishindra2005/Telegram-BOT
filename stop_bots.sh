#!/bin/bash

# TElegram-BOT Shutdown Script
# This script stops all running bot instances

echo "🛑 Stopping TElegram-BOT System..."

# Check if we have saved PIDs
if [ -f .bot_pids ]; then
    # Read PIDs from file
    read -r VARSHA_PID COLLEGE_PID NETWORK_PID < .bot_pids
    
    # Stop each bot
    if ps -p $VARSHA_PID > /dev/null 2>&1; then
        echo "🔮 Stopping Varsha Bot (PID: $VARSHA_PID)..."
        kill $VARSHA_PID
        echo "✅ Varsha Bot stopped"
    else
        echo "⚠️ Varsha Bot not running"
    fi
    
    if ps -p $COLLEGE_PID > /dev/null 2>&1; then
        echo "🎓 Stopping College Bot (PID: $COLLEGE_PID)..."
        kill $COLLEGE_PID
        echo "✅ College Bot stopped"
    else
        echo "⚠️ College Bot not running"
    fi
    
    if ps -p $NETWORK_PID > /dev/null 2>&1; then
        echo "🌐 Stopping Network Monitor (PID: $NETWORK_PID)..."
        kill $NETWORK_PID
        echo "✅ Network Monitor stopped"
    else
        echo "⚠️ Network Monitor not running"
    fi
    
    # Remove PID file
    rm .bot_pids
else
    # If no PID file, try to find and kill all python instances
    echo "⚠️ No PID file found, attempting to stop all Python processes..."
    pkill -f "python3 gem3.py"
    pkill -f "python3 rishi_mn.py"
    pkill -f "python3 net.py"
fi

echo -e "\n✅ All bots have been stopped"
echo "Current Python processes:"
ps aux | grep "[p]ython3"

# Make the script executable
chmod +x stop_bots.sh 