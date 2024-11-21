arkana: .arkana
.arkana:
	git clone https://github.com/svmpsp/arkana-build-tools.git .arkana_out
	mkdir -p .arkana/makefiles
	cp -r .arkana_out/arkana-build-tools/makefiles .arkana/
	rm -rf .arkana_out

include .arkana/makefiles/common.mk
include .arkana/makefiles/python.mk

debug:
	poetry run exerpyse --debug start