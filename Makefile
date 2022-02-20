INSTALL_DIR := /tmp

all: install

install:
	cp alert.py canyon-alerter.sh telegram.sh ${INSTALL_DIR}/
	cp canyon-alerter.{service,timer} ~/.config/systemd/user/
	systemctl --user daemon-reload
	systemctl --user enable canyon-alerter.service
	systemctl --user enable canyon-alerter.timer
	systemctl --user start canyon-alerter.service
	systemctl --user start canyon-alerter.timer

clean:
	systemctl --user disable canyon-alerter.service
	systemctl --user disable canyon-alerter.timer
	rm ~/.config/systemd/user/canyon-alerter.*
	systemctl --user daemon-reload
	rm ${INSTALL_DIR}/alert.py ${INSTALL_DIR}/canyon-alerter.sh ${INSTALL_DIR}/telegram.sh