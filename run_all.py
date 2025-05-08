print("""
[+] Advanced Pentest Toolkit
1. فحص المنافذ
2. مراقبة ARP
3. جمع نطاقات فرعية
4. معلومات من فيسبوك
5. كشف هجمات Deauth
""")
choice = input("اختر الأداة (رقم): ")

if choice == "1":
    import tools.port_scanner as tool
elif choice == "2":
    import tools.arp_sniffer as tool
elif choice == "3":
    import tools.subdomain_finder as tool
elif choice == "4":
    import tools.facebook_osint as tool
elif choice == "5":
    import tools.wifi_deauth_detector as tool
else:
    print("خيار غير صالح")
    exit()

tool.main()
