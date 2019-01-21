#!/bin/bash
echo a | ./bestrong
echo =========================OR============================
for i in $(seq 1 1 1000)
do
	echo $i | ./bestrong | grep -oE inctfj{.*}
done
