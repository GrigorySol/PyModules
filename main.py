from Utilites import passcheck

hashes = passcheck.get_hashes_for_password("any_password")
print(hashes[0])
print()
print(passcheck.compare_password_hash(*hashes))
