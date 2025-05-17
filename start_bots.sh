#!/bin/bash

# TElegram-BOT Startup Script
# This script starts all the bots in the background

echo "🤖 Starting TElegram-BOT System..."

# Create logs directory if it doesn't exist
mkdir -p logs

# Start each bot in background with logs
echo "🔮 Starting Varsha Bot (Personal Companion)..."
nohup python3 gem3.py > logs/varsha_bot.log 2>&1 &
VARSHA_PID=$!
echo "✅ Varsha Bot started with PID: $VARSHA_PID"

echo "🎓 Starting College Bot (Application Assistant)..."
nohup python3 rishi_mn.py > logs/college_bot.log 2>&1 &
COLLEGE_PID=$!
echo "✅ College Bot started with PID: $COLLEGE_PID"

echo "🌐 Starting Network Monitor..."
nohup python3 net.py > logs/network_monitor.log 2>&1 &
NETWORK_PID=$!
echo "✅ Network Monitor started with PID: $NETWORK_PID"

echo -e "\n🚀 All systems are running! Check logs in the logs directory."
echo "To view logs: tail -f logs/varsha_bot.log"
echo "To stop all bots: ./stop_bots.sh or 'pkill -f python3'"
echo -e "\nBot Status:"
ps aux | grep "[p]ython3 "

# Save PIDs for stop script
echo "$VARSHA_PID $COLLEGE_PID $NETWORK_PID" > .bot_pids

# Make the process executable
chmod +x start_bots.sh 