#!/usr/bin/env bash
# Ahmed Gado (ahmedehabg@gmail.com) 24/03/2019
# Installs ADInstruments Spirometry module for Lab Charts Reader.
# Normally, it is only available for Lab Charts (the paid version).
# This script overcomes this limitation.
# Use at your own risk.
echo "🍺 This script is going to download the Spirometry module and make it
available for the Lab Charts Reader software to use. Use at your own
risk."

read -p "🍺 Are you sure that you want to continue? (y/n)" -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
  curl -o ./Spirometry.zip www.upgado.com/uploads/Spirometry.zip

else
  echo "Aborted"
fi
