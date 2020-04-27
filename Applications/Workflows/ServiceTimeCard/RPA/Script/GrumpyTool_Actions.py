import re

class GrumpyTool_Actions:

    def customised_grumpy_url(doc_id):
        url_for_doc_id="http://grumpys/cgi-bin/webtools/documenttool.pl?poappkey="+str(doc_id)+"&pouser=&podocid=&showdetails=on"
        return url_for_doc_id

    def get_evision_docid(driver):
        data=driver.find_element_by_xpath(".//small[2]").text


        print(data)