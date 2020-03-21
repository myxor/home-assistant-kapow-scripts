
Configure home-assistant:

    rest_command:
      raspberry_pi_reboot:
        url: 'http://192.168.188.58:3000/reboot'
      raspberry_pi_poweroff:
        url: 'http://192.168.188.58:3000/poweroff'
      raspberry_pi_shutdown:
        url: 'http://192.168.188.58:3000/shutdown'
