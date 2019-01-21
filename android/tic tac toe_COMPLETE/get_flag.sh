#!/bin/bash
apktool d T3.apk
grep -roE inctfj{.*}
