from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="##AF.v4.1.0", parents=()),
    ConfigLine(config_line="afnetconf.1.atpctarget=0", parents=()),
    ConfigLine(config_line="afnetconf.1.autoneg=enabled", parents=()),
    ConfigLine(config_line="afnetconf.1.carrierdrop=off", parents=()),
    ConfigLine(config_line="afnetconf.1.carrierdropdebounce=0", parents=()),
    ConfigLine(config_line="afnetconf.1.carrierdropto=5", parents=()),
    ConfigLine(config_line="afnetconf.1.cdblockafterpulse=disabled", parents=()),
    ConfigLine(config_line="afnetconf.1.cdfirstsessiontimer=0", parents=()),
    ConfigLine(config_line="afnetconf.1.cdfirstsessionwait=disabled", parents=()),
    ConfigLine(config_line="afnetconf.1.cdtracknosession=disabled", parents=()),
    ConfigLine(config_line="afnetconf.1.devname=af0", parents=()),
    ConfigLine(config_line="afnetconf.1.flowcntl=disabled", parents=()),
    ConfigLine(config_line="afnetconf.1.mcastfilter=disabled", parents=()),
    ConfigLine(config_line="afnetconf.1.mincapholdoff=0", parents=()),
    ConfigLine(config_line="afnetconf.1.mincapholdoffup=0", parents=()),
    ConfigLine(config_line="afnetconf.1.minrxcapacity=0", parents=()),
    ConfigLine(config_line="afnetconf.1.minrxcapacityup=0", parents=()),
    ConfigLine(config_line="afnetconf.1.mintxcapacity=0", parents=()),
    ConfigLine(config_line="afnetconf.1.mintxcapacityup=0", parents=()),
    ConfigLine(config_line="afnetconf.1.status=enabled", parents=()),
    ConfigLine(config_line="afnetconf.status=enabled", parents=()),
    ConfigLine(config_line="airview.tcp_port=18888", parents=()),
    ConfigLine(config_line="airview.tcpport=18888", parents=()),
    ConfigLine(config_line="bridge.1.devname=br0", parents=()),
    ConfigLine(config_line="bridge.1.fd=1", parents=()),
    ConfigLine(config_line="bridge.1.port.1.devname=eth0", parents=()),
    ConfigLine(config_line="bridge.1.port.1.status=enabled", parents=()),
    ConfigLine(config_line="bridge.1.port.2.devname=air0", parents=()),
    ConfigLine(config_line="bridge.1.port.2.status=enabled", parents=()),
    ConfigLine(config_line="bridge.1.status=enabled", parents=()),
    ConfigLine(config_line="bridge.1.stp.status=disabled", parents=()),
    ConfigLine(config_line="bridge.status=enabled", parents=()),
    ConfigLine(config_line="dhcpc.1.devname=eth0", parents=()),
    ConfigLine(config_line="dhcpc.1.status=disabled", parents=()),
    ConfigLine(config_line="dhcpc.2.devname=air0", parents=()),
    ConfigLine(config_line="dhcpc.2.status=disabled", parents=()),
    ConfigLine(config_line="dhcpc.3.devname=br0", parents=()),
    ConfigLine(config_line="dhcpc.3.status=disabled", parents=()),
    ConfigLine(config_line="dhcpc.status=disabled", parents=()),
    ConfigLine(config_line="discovery.cdp.status=disabled", parents=()),
    ConfigLine(config_line="discovery.status=enabled", parents=()),
    ConfigLine(config_line="dyndns.status=disabled", parents=()),
    ConfigLine(config_line="ebtables.status=enabled", parents=()),
    ConfigLine(config_line="ebtables.sys.arpnat.status=disabled", parents=()),
    ConfigLine(config_line="ebtables.sys.eap.status=disabled", parents=()),
    ConfigLine(config_line="ebtables.sys.status=enabled", parents=()),
    ConfigLine(config_line="gui.language=en_US", parents=()),
    ConfigLine(config_line="httpd.https.port=443", parents=()),
    ConfigLine(config_line="httpd.https.status=disabled", parents=()),
    ConfigLine(config_line="httpd.port=80", parents=()),
    ConfigLine(config_line="httpd.session.timeout=300", parents=()),
    ConfigLine(config_line="httpd.status=enabled", parents=()),
    ConfigLine(config_line="netconf.1.allmulti=disabled", parents=()),
    ConfigLine(config_line="netconf.1.autoip.status=disabled", parents=()),
    ConfigLine(config_line="netconf.1.autoneg=enabled", parents=()),
    ConfigLine(config_line="netconf.1.devname=eth0", parents=()),
    ConfigLine(config_line="netconf.1.hwaddr.mac=", parents=()),
    ConfigLine(config_line="netconf.1.hwaddr.status=disabled", parents=()),
    ConfigLine(config_line="netconf.1.ip=0.0.0.0", parents=()),
    ConfigLine(config_line="netconf.1.mtu=1500", parents=()),
    ConfigLine(config_line="netconf.1.netmask=255.255.255.0", parents=()),
    ConfigLine(config_line="netconf.1.promisc=enabled", parents=()),
    ConfigLine(config_line="netconf.1.role=bridge_port", parents=()),
    ConfigLine(config_line="netconf.1.status=enabled", parents=()),
    ConfigLine(config_line="netconf.1.up=enabled", parents=()),
    ConfigLine(config_line="netconf.2.allmulti=disabled", parents=()),
    ConfigLine(config_line="netconf.2.autoip.status=disabled", parents=()),
    ConfigLine(config_line="netconf.2.devname=air0", parents=()),
    ConfigLine(config_line="netconf.2.hwaddr.mac=", parents=()),
    ConfigLine(config_line="netconf.2.hwaddr.status=disabled", parents=()),
    ConfigLine(config_line="netconf.2.ip=0.0.0.0", parents=()),
    ConfigLine(config_line="netconf.2.mtu=1500", parents=()),
    ConfigLine(config_line="netconf.2.netmask=255.255.255.0", parents=()),
    ConfigLine(config_line="netconf.2.promisc=enabled", parents=()),
    ConfigLine(config_line="netconf.2.role=bridge_port", parents=()),
    ConfigLine(config_line="netconf.2.status=enabled", parents=()),
    ConfigLine(config_line="netconf.2.up=enabled", parents=()),
    ConfigLine(config_line="netconf.3.allmulti=disabled", parents=()),
    ConfigLine(config_line="netconf.3.autoip.status=disabled", parents=()),
    ConfigLine(config_line="netconf.3.devname=br0", parents=()),
    ConfigLine(config_line="netconf.3.hwaddr.mac=", parents=()),
    ConfigLine(config_line="netconf.3.hwaddr.status=disabled", parents=()),
    ConfigLine(config_line="netconf.3.ip=10.10.10.10", parents=()),
    ConfigLine(config_line="netconf.3.mtu=1500", parents=()),
    ConfigLine(config_line="netconf.3.netmask=255.255.255.0", parents=()),
    ConfigLine(config_line="netconf.3.role=mlan", parents=()),
    ConfigLine(config_line="netconf.3.status=enabled", parents=()),
    ConfigLine(config_line="netconf.3.up=enabled", parents=()),
    ConfigLine(config_line="netconf.status=enabled", parents=()),
    ConfigLine(config_line="netmode=airfiber", parents=()),
    ConfigLine(config_line="ntpclient.status=disabled", parents=()),
    ConfigLine(config_line="ppp.status=disabled", parents=()),
    ConfigLine(config_line="pwdog.delay=300", parents=()),
    ConfigLine(config_line="pwdog.host=", parents=()),
    ConfigLine(config_line="pwdog.period=300", parents=()),
    ConfigLine(config_line="pwdog.retry=3", parents=()),
    ConfigLine(config_line="pwdog.status=disabled", parents=()),
    ConfigLine(config_line="radio.1.antenna.gain=33", parents=()),
    ConfigLine(config_line="radio.1.atpctarget=0", parents=()),
    ConfigLine(config_line="radio.1.cable.loss=0", parents=()),
    ConfigLine(config_line="radio.1.countrycode=840", parents=()),
    ConfigLine(config_line="radio.1.dfsthreshold=0", parents=()),
    ConfigLine(config_line="radio.1.dualfreqmode=enabled", parents=()),
    ConfigLine(config_line="radio.1.duplex=half", parents=()),
    ConfigLine(config_line="radio.1.dutycycle=50", parents=()),
    ConfigLine(config_line="radio.1.framelength=-1", parents=()),
    ConfigLine(config_line="radio.1.gps_sync=disabled", parents=()),
    ConfigLine(config_line="radio.1.key=s:password1", parents=()),
    ConfigLine(config_line="radio.1.linkname=UBNT", parents=()),
    ConfigLine(config_line="radio.1.mode=slave", parents=()),
    ConfigLine(config_line="radio.1.pwrbackoff=disabled", parents=()),
    ConfigLine(config_line="radio.1.pwrout.10x=0", parents=()),
    ConfigLine(config_line="radio.1.pwrout.4x=43", parents=()),
    ConfigLine(config_line="radio.1.pwrout.6x=43", parents=()),
    ConfigLine(config_line="radio.1.pwrout.8x=33", parents=()),
    ConfigLine(config_line="radio.1.rate.auto=enabled", parents=()),
    ConfigLine(config_line="radio.1.rate=6x", parents=()),
    ConfigLine(config_line="radio.1.rfrate=6x", parents=()),
    ConfigLine(config_line="radio.1.rx_freq10=null", parents=()),
    ConfigLine(config_line="radio.1.rx_freq2=null", parents=()),
    ConfigLine(config_line="radio.1.rx_freq3=null", parents=()),
    ConfigLine(config_line="radio.1.rx_freq4=null", parents=()),
    ConfigLine(config_line="radio.1.rx_freq5=null", parents=()),
    ConfigLine(config_line="radio.1.rx_freq6=null", parents=()),
    ConfigLine(config_line="radio.1.rx_freq7=null", parents=()),
    ConfigLine(config_line="radio.1.rx_freq8=null", parents=()),
    ConfigLine(config_line="radio.1.rx_freq9=null", parents=()),
    ConfigLine(config_line="radio.1.rx_freq=24.1GHz", parents=()),
    ConfigLine(config_line="radio.1.rxchanbw=2048", parents=()),
    ConfigLine(config_line="radio.1.rxgain=low", parents=()),
    ConfigLine(config_line="radio.1.sharedant=disabled", parents=()),
    ConfigLine(config_line="radio.1.sisomode=disabled", parents=()),
    ConfigLine(config_line="radio.1.status=enabled", parents=()),
    ConfigLine(config_line="radio.1.streammode=disabled", parents=()),
    ConfigLine(config_line="radio.1.subsystemid=0xaf01", parents=()),
    ConfigLine(config_line="radio.1.tx_freq2=null", parents=()),
    ConfigLine(config_line="radio.1.tx_freq3=null", parents=()),
    ConfigLine(config_line="radio.1.tx_freq=24.1GHz", parents=()),
    ConfigLine(config_line="radio.1.txchanbw=2048", parents=()),
    ConfigLine(config_line="radio.1.txpower=33", parents=()),
    ConfigLine(config_line="radio.countrycode=840", parents=()),
    ConfigLine(config_line="radio.status=enabled", parents=()),
    ConfigLine(config_line="resolv.host.1.name=UBNT", parents=()),
    ConfigLine(config_line="resolv.host.1.status=enabled", parents=()),
    ConfigLine(config_line="resolv.nameserver.1.ip=1.1.1.1", parents=()),
    ConfigLine(config_line="resolv.nameserver.1.status=enabled", parents=()),
    ConfigLine(config_line="resolv.nameserver.2.ip=", parents=()),
    ConfigLine(config_line="resolv.nameserver.2.status=disabled", parents=()),
    ConfigLine(config_line="resolv.nameserver.status=enabled", parents=()),
    ConfigLine(config_line="resolv.status=disabled", parents=()),
    ConfigLine(config_line="route.1.comment=", parents=()),
    ConfigLine(config_line="route.1.devname=br0", parents=()),
    ConfigLine(config_line="route.1.gateway=10.10.10.1", parents=()),
    ConfigLine(config_line="route.1.ip=0.0.0.0", parents=()),
    ConfigLine(config_line="route.1.netmask=0", parents=()),
    ConfigLine(config_line="route.1.status=enabled", parents=()),
    ConfigLine(config_line="route.status=enabled", parents=()),
    ConfigLine(config_line="snmp.community=admin", parents=()),
    ConfigLine(config_line="snmp.contact=lab", parents=()),
    ConfigLine(config_line="snmp.location=lab", parents=()),
    ConfigLine(config_line="snmp.status=enabled", parents=()),
    ConfigLine(config_line="sshd.auth.passwd=enabled", parents=()),
    ConfigLine(config_line="sshd.port=22", parents=()),
    ConfigLine(config_line="sshd.status=enabled", parents=()),
    ConfigLine(config_line="syslog.remote.port=514", parents=()),
    ConfigLine(config_line="syslog.remote.status=disabled", parents=()),
    ConfigLine(config_line="syslog.status=disabled", parents=()),
    ConfigLine(config_line="system.button.reset=enabled", parents=()),
    ConfigLine(config_line="system.cfg.version=65540", parents=()),
    ConfigLine(config_line="system.date.status=disabled", parents=()),
    ConfigLine(config_line="system.date.timestamp=", parents=()),
    ConfigLine(config_line="system.eirp.status=enabled", parents=()),
    ConfigLine(config_line="system.latitude=", parents=()),
    ConfigLine(config_line="system.longitude=", parents=()),
    ConfigLine(config_line="system.timezone=GMT", parents=()),
    ConfigLine(config_line="telnetd.port=23", parents=()),
    ConfigLine(config_line="telnetd.status=enabled", parents=()),
    ConfigLine(config_line="ucode.1.rxscramblekey=0", parents=()),
    ConfigLine(config_line="ucode.1.txscramblekey=0", parents=()),
    ConfigLine(config_line="udapi_bridge.callhome.status=disabled", parents=()),
    ConfigLine(config_line="unms.uri=-", parents=()),
    ConfigLine(config_line="update.check.status=enabled", parents=()),
    ConfigLine(config_line="users.1.name=ubnt", parents=()),
    ConfigLine(config_line="users.1.password=$1$YSWw8TsR$eBl/.jP1ibig8DUF4nn65.", parents=()),
    ConfigLine(config_line="users.1.status=enabled", parents=()),
    ConfigLine(config_line="users.2.status=disabled", parents=()),
    ConfigLine(config_line="users.status=enabled", parents=()),
    ConfigLine(config_line="vlan.status=disabled", parents=()),
]
