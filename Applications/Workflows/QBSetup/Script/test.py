



def get(adaptor,doc):
    Quickbooks={"810":["SPS QuickBooks Adaptor | RSX 7.2 | 810 - Legacy","106968"],"850":["SPS QuickBooks Adaptor | RSX 7.2 | 850 - Legacy","106967"],"875":["SPS QuickBooks Adaptor | RSX 7.2 | 875 - Legacy","110240"],"856":["SPS Quickbooks Adapter RSX 7.2 | OzLink | 856","135124"]}
    Fishbowl={"810":["SPS Fishbowl Adaptor | RSX 7.2 | 810 - Legacy","109097"],"850":["SPS Fishbowl Adaptor | RSX 7.2 | 850 - Legacy","109095"],"875":["SPS FISHBOWL ADAPTOR | RSX 7.2 | 875 - LEGACY","112556"],"856":["SPS Fishbowl Adaptor | RSX 7.2 | 856 - Legacy","109096"]}
    Dwyer={"810":["Dwyer Adaptor V7 810 XML","31788"],"850":["Dwyer Adaptor V7 850 XML","31768"],"875":["Dwyer Adaptor V7 875 XML","70230"]}
    Peachtree={"810":["Peachtree 810 XML","73633"],"850":["Peachtree 850 XML","73632"],"875":["Peachtree 875 XML","78248"]}
    try:
        if adaptor=="Quickbooks":
            arr=Quickbooks.get(doc)
            return arr
        if adaptor=="Fishbowl":
            arr=Fishbowl.get(doc)
            return arr
        if adaptor=="Dwyer":
            arr=Dwyer.get(doc)
            return arr
        if adaptor=="Peachtree":
            arr=Peachtree.get(doc)
            return arr
    except:
        print("in excep")
        return ['none','nnn']
cap=get("Quickbooks","850")
print(cap[0])