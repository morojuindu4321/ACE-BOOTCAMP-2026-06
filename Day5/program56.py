with open("/workspaces/ACE-BOOTCAMP-2026-06/Day5/program52.py",'rb') as f:
    content = f.readline(2000)
    with open("/workspaces/ACE-BOOTCAMP-2026-06/Day5/program52.py","wb") as cf:
        while  len(content) > 0:
            cf.write(content)
            content=f.read(2000)