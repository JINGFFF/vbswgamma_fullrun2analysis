export PATH="${PATH}:${PWD}/aqgc"
export PATH="${PATH}:${PWD}/fakephoton"
export PATH="${PATH}:${PWD}/make_datacard"
export PATH="${PATH}:${PWD}/uncertainty"
export PATH="${PATH}:${PWD}/condor"
export PYTHONPATH="$PYTHONPATH:${PWD}/uncertainty"
chmod +x aqgc/*py
chmod +x fakephoton/*py
chmod +x make_datacard/*py
chmod +x uncertainty/*py 
chmod +x condor/*py
