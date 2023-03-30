speed=float(input("Enter speed of in KM:"))
if speed<=70:
    print("OK")
else:
    d_points=str((speed-70)/5)
    print("Points:", d_points)
    if float(d_points)>12:
        print("License Suspended")

