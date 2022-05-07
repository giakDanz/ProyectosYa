#Send post to webscrapper

import requests
import json
import re

from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
import requests
#using an url , in hearder have Content-Type:  application/x-www-form-urlencoded, 
# and in body have the data to send ctl00$CPH1$DrpYear:2022 ,ctl00$CPH1$DrpActProy:Proyecto ,__VIEWSTATE:/wEPDwUJMjk5MzYzMDMzDxYKHg1TZWxlY3RlZExldmVsCylJRHdoTGV2ZWwsIEFwcF9Db2RlLCBWZXJzaW9uPTAuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbBUeDlNlbGVjdGVkTGV2ZWxzBQYwPSYyMT0eDE90aGVyRmlsdGVycwUkeT0yMDIyJmFwPVByb3llY3RvJmNwYWdlPTEmcHNpemU9NDAwHghTZWFyY2hCeQspSVNlYXJjaEJ5LCBBcHBfQ29kZSwgVmVyc2lvbj0wLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGwAHgpTZWFyY2hUZXh0ZRYCZg9kFgICAw9kFgQCBQ88KwAGAQAPFgIeClRhYk9uSW5kZXhmZGQCBw9kFggCAQ9kFgQCBw8QDxYCHgtfIURhdGFCb3VuZGcWAh4Ib25jaGFuZ2UFFU9uQ2hhbmdlRHJwWWVhcih0aGlzKRAVGAQxOTk5BDIwMDAEMjAwMQQyMDAyBDIwMDMEMjAwNAQyMDA1BDIwMDYEMjAwNwQyMDA4BDIwMDkEMjAxMAQyMDExBDIwMTIEMjAxMwQyMDE0BDIwMTUEMjAxNgQyMDE3BDIwMTgEMjAxOQQyMDIwBDIwMjEEMjAyMhUYBDE5OTkEMjAwMAQyMDAxBDIwMDIEMjAwMwQyMDA0BDIwMDUEMjAwNgQyMDA3BDIwMDgEMjAwOQQyMDEwBDIwMTEEMjAxMgQyMDEzBDIwMTQEMjAxNQQyMDE2BDIwMTcEMjAxOAQyMDE5BDIwMjAEMjAyMQQyMDIyFCsDGGdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAgkPEA9kFgIfBwUYT25DaGFuZ2VEcnBBY3RQcm95KHRoaXMpZGRkAgIPZBYIAiEPDxYCHgdWaXNpYmxlZ2RkAiMPDxYCHwhoZGQCLw8PFgIfCGdkZAI/Dw8WAh8IaGRkAgQPZBYCZg9kFgYCAQ9kFgRmD2QWCgICDw8WBB4HQ2VsbEFyZwUEY29sMR4HVG9vbFRpcAUlUHJlc3VwdWVzdG8gSW5zdGl0dWNpb25hbCBkZSBBcGVydHVyYWQWBGYPFQEDUElBZAIBD2QWAgIBDxYCHg5Qb3B1cENvbnRyb2xJRAUGUG5sUElBZAIDDw8WBB8JBQRjb2wyHwoFJFByZXN1cHVlc3RvIEluc3RpdHVjaW9uYWwgTW9kaWZpY2Fkb2QWBGYPFQEDUElNZAIBD2QWAgIBDxYCHwsFBlBubFBJTWQCBA8PFgQfCQUEY29sOB8KZGQWBGYPFQEOQ2VydGlmaWNhY2nDs25kAgEPZBYCAgEPFgIfCwUQUG5sQ2VydGlmaWNhY2lvbmQCBQ8PFgQfCQUEY29sMx8KZGQWBGYPFQEQQ29tcHJvbWlzbyBBbnVhbGQCAQ9kFgICAQ8WAh8LBQxQbmxDb21wQW51YWxkAgcPDxYEHwkFBGNvbDcfCmRkFgJmDxUBCEF2YW5jZSAlZAIBD2QWBmYPDxYEHwkFBGNvbDQfCmRkFgJmDxUBH0F0ZW5jacOzbiBkZSBDb21wcm9taXNvIE1lbnN1YWxkAgEPDxYEHwkFBGNvbDUfCmRkFgJmDxUBCURldmVuZ2Fkb2QCAg8PFgQfCQUEY29sNh8KZGQWAmYPFQEGR2lyYWRvZAIDDw8WAh8IZ2QWAgIJDw8WAh8IaGRkAgUPDxYCHwhoZBYCAgEPPCsABwEADxYGHghQYWdlU2l6ZQKQAx4LQ3VycmVudFBhZ2UCAR4JSXRlbUNvdW50AhpkFgJmD2QWAgITDw8WAh4EVGV4dAUBMWRkAgkPDxYCHw8FEzA0IGRlIG1heW8gZGUgMjAyMi5kZGTagoE4zLrxNiFIygRdgTBl78Yi2usS2pkPAEHAgd4cZg== ,__EVENTVALIDATION:/wEdACmlAADDR9QwJaaeg+VXaYSs5EdtbTHqfmqN1rp7Gf0xZSQ8TBsjUqNP7PZB7LXAwUxi1+RQQgFa7RCJSHKoIh8bkF9q1EGo6Oi6DTPyBDKoS9XLHxff3Ik9aTo789+FO0AfoMvnz7K3WQv+WuErvE5fNiszC6wQ5ste1/jV76Q4VvZqkrjYVtxKRHqCMZl4f7BeXYIGkvHq6nMIHcevvSVm0yWGCmhBUACBaC6uFR2XCotGnxduM3+h9gZS8BdfBruDGU89IQjdPnzsJekPA7z+gdKl+8havS5rYkzEbc/TBS6gPDGQvCN5sy0oun/v6kfQ2NgviJjarn9pF00iIc1+MsIHlJEPXUKjNdahAoyYBXn1il1SYJL8WVTNp+J8jX4StOnUp9Zq98S/oku7tbh82mhqVxaWBTExaoXx0r2v55wqaW3+pi6+Lx2mIaX4x5rngllvizktMYSvEMR8GStg0HD9YELOAQGJQqNt2ku2JdYRAr9ohmWpibcW4TTWMBxO5w7IIe25oKz1c0u0pSYn9EZv2sI13MVDhH84bT3lcEJvbtH8nSW6n8fmvBkY2Zz61Jxn+R9jfjVJerpHRoeArDZlyTyRZqbf+41nghXjjqQnKLWKzCDXdzJwKxJk73mr9lP8KQhwOE5MAGbHRFxFtZyuB47qiJPkLre+EtbR438UByklEYO0QVYZV2PQW+vC+kK/vGnv3JqbRwMaYh6yetGtxXLOCDxqt0pk8Q5bFHYYqP1BddHzbn+N/BU4Wb1A45Iy5m48s0OxA4xoinjFYEKdrPagKHzopY90suIQyCHEhzut07raMFC8K0S2P23QzabNiRJP67fFYNfEZ4Qd7mjH5RhKFrQdBnweNNoczmZFqKHF0pVS0Z/BCPh5dvy1myTOYBzLmY2opfp1JYCB

#Nivel Lima Metropolitana
#Lima:15/1449006935/1723619836/609617196.54/564767492.25/468964036.86/450919322.95/826915821.53
def scrapper(url):
    #Send post to webscrapper
    #using an url , in hearder have Content-Type:  application/x-www-form-urlencoded, 
    # and in body have the data to send ctl00$CPH1$DrpYear:2022 ,ctl00$CPH1$DrpActProy:Proyecto ,__VIEWSTATE:/wEPDwUJMjk5MzYzMDMzDxYKHg1TZWxlY3RlZExldmVsCylJRHdoTGV2ZWwsIEFwcF9Db2RlLCBWZXJzaW9uPTAuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbBUeDlNlbGVjdGVkTGV2ZWxzBQYwPSYyMT0eDE90aGVyRmlsdGVycwUkeT0yMDIyJmFwPVByb3llY3RvJmNwYWdlPTEmcHNpemU9NDAwHghTZWFyY2hCeQspSVNlYXJjaEJ5LCBBcHBfQ29kZSwgVmVyc2lvbj0wLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGwAHgpTZWFyY2hUZXh0ZRYCZg9kFgICAw9kFgQCBQ88KwAGAQAPFgIeClRhYk9uSW5kZXhmZGQCBw9kFggCAQ9kFgQCBw8QDxYCHgtfIURhdGFCb3VuZGcWAh4Ib25jaGFuZ2UFFU9uQ2hhbmdlRHJwWWVhcih0aGlzKRAVGAQxOTk5BDIwMDAEMjAwMQQyMDAyBDIwMDMEMjAwNAQyMDA1BDIwMDYEMjAwNwQyMDA4BDIwMDkEMjAxMAQyMDExBDIwMTIEMjAxMwQyMDE0BDIwMTUEMjAxNgQyMDE3BDIwMTgEMjAxOQQyMDIwBDIwMjEEMjAyMhUYBDE5OTkEMjAwMAQyMDAxBDIwMDIEMjAwMwQyMDA0BDIwMDUEMjAwNgQyMDA3BDIwMDgEMjAwOQQyMDEwBDIwMTEEMjAxMgQyMDEzBDIwMTQEMjAxNQQyMDE2BDIwMTcEMjAxOAQyMDE5BDIwMjAEMjAyMQQyMDIyFCsDGGdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAgkPEA9kFgIfBwUYT25DaGFuZ2VEcnBBY3RQcm95KHRoaXMpZGRkAgIPZBYIAiEPDxYCHgdWaXNpYmxlZ2RkAiMPDxYCHwhoZGQCLw8PFgIfCGdkZAI/Dw8WAh8IaGRkAgQPZBYCZg9kFgYCAQ9kFgRmD2QWCgICDw8WBB4HQ2VsbEFyZwUEY29sMR4HVG9vbFRpcAUlUHJlc3VwdWVzdG8gSW5zdGl0dWNpb25hbCBkZSBBcGVydHVyYWQWBGYPFQEDUElBZAIBD2QWAgIBDxYCHg5Qb3B1cENvbnRyb2xJRAUGUG5sUElBZAIDDw8WBB8JBQRjb2wyHwoFJFByZXN1cHVlc3RvIEluc3RpdHVjaW9uYWwgTW9kaWZpY2Fkb2QWBGYPFQEDUElNZAIBD2QWAgIBDxYCHwsFBlBubFBJTWQCBA8PFgQfCQUEY29sOB8KZGQWBGYPFQEOQ2VydGlmaWNhY2nDs25kAgEPZBYCAgEPFgIfCwUQUG5sQ2VydGlmaWNhY2lvbmQCBQ8PFgQfCQUEY29sMx8KZGQWBGYPFQEQQ29tcHJvbWlzbyBBbnVhbGQCAQ9kFgICAQ8WAh8LBQxQbmxDb21wQW51YWxkAgcPDxYEHwkFBGNvbDcfCmRkFgJmDxUBCEF2YW5jZSAlZAIBD2QWBmYPDxYEHwkFBGNvbDQfCmRkFgJmDxUBH0F0ZW5jacOzbiBkZSBDb21wcm9taXNvIE1lbnN1YWxkAgEPDxYEHwkFBGNvbDUfCmRkFgJmDxUBCURldmVuZ2Fkb2QCAg8PFgQfCQUEY29sNh8KZGQWAmYPFQEGR2lyYWRvZAIDDw8WAh8IZ2QWAgIJDw8WAh8IaGRkAgUPDxYCHwhoZBYCAgEPPCsABwEADxYGHghQYWdlU2l6ZQKQAx4LQ3VycmVudFBhZ2UCAR4JSXRlbUNvdW50AhpkFgJmD2QWAgITDw8WAh4EVGV4dAUBMWRkAgkPDxYCHw8FEzA0IGRlIG1heW8gZGUgMjAyMi5kZGTagoE4zLrxNiFIygRdgTBl78Yi2usS2pkPAEHAgd4cZg== ,__EVENTVALIDATION:/wEdACmlAADDR9QwJaaeg+VXaYSs5EdtbTHqfmqN1rp7Gf0xZSQ8TBsjUqNP7PZB7LXAwUxi1+RQQgFa7RCJSHKoIh8bkF9q1EGo6Oi6DTPyBDKoS9XLHxff3Ik9aTo789+FO0AfoMvnz7K3WQv+WuErvE5fNiszC6wQ5ste1/jV76Q4VvZqkrjYVtxKRHqCMZl4f7BeXYIGkvHq6nMIHcevvSVm0yWGCmhBUACBaC6uFR2XCotGnxduM3+h9gZS8BdfBruDGU89IQjdPnzsJekPA7z+gdKl+8havS5rYkzEbc/TBS6gPDGQvCN5sy0oun/v6kfQ2NgviJjarn9pF00iIc1+MsIHlJEPXUKjNdahAoyYBXn1il1SYJL8WVTNp+J8jX4StOnUp9Zq98S/oku7tbh82mhqVxaWBTExaoXx0r2v55wqaW3+pi6+Lx2mIaX4x5rngllvizktMYSvEMR8GStg0HD9YELOAQGJQqNt2ku2JdYRAr9ohmWpibcW4TTWMBxO5w7IIe25oKz1c0u0pSYn9EZv2sI13MVDhH84bT3lcEJvbtH8nSW6n8fmvBkY2Zz61Jxn+R9jfjVJerpHRoeArDZlyTyRZqbf+41nghXjjqQnKLWKzCDXdzJwKxJk73mr9lP8KQhwOE5MAGbHRFxFtZyuB47qiJPkLre+EtbR438UByklEYO0QVYZV2PQW+vC+kK/vGnv3JqbRwMaYh6yetGtxXLOCDxqt0pk8Q5bFHYYqP1BddHzbn+N/BU4Wb1A45Iy5m48s0OxA4xoinjFYEKdrPagKHzopY90suIQyCHEhzut07raMFC8K0S2P23QzabNiRJP67fFYNfEZ4Qd7mjH5RhKFrQdBnweNNoczmZFqKHF0pVS0Z/BCPh5dvy1myTOYBzLmY2opfp1JYCB

    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    ##use header in post request. in hearder have Content-Type:  application/x-www-form-urlencoded
    ##post request to get the html content of the url

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    #use body in post request, __VIEWSTATE is the key

    body = {
        'ctl00$CPH1$DrpYear':'2022' ,
        'ctl00$CPH1$DrpActProy':'Proyecto' ,
        'ctl00$CPH1$BtnProdProy':'Producto/Proyecto' ,
        ##especified the key of the deparment
        'grp1':'15/1449006935/1723619836/609617196.54/564767492.25/468964036.86/450919322.95/826915821.53',
        '__VIEWSTATE':'/wEPDwUJMjk5MzYzMDMzDxYKHg1TZWxlY3RlZExldmVsCylJRHdoTGV2ZWwsIEFwcF9Db2RlLCBWZXJzaW9uPTAuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbBUeDlNlbGVjdGVkTGV2ZWxzBQowPSYxPVImMjE9HgxPdGhlckZpbHRlcnMFJHk9MjAyMiZhcD1Qcm95ZWN0byZjcGFnZT0xJnBzaXplPTQwMB4IU2VhcmNoQnkLKUlTZWFyY2hCeSwgQXBwX0NvZGUsIFZlcnNpb249MC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsAB4KU2VhcmNoVGV4dGUWAmYPZBYCAgMPZBYEAgUPPCsABgEADxYCHgpUYWJPbkluZGV4ZmRkAgcPZBYIAgEPZBYEAgcPEA8WAh4LXyFEYXRhQm91bmRnFgIeCG9uY2hhbmdlBRVPbkNoYW5nZURycFllYXIodGhpcykQFRgEMTk5OQQyMDAwBDIwMDEEMjAwMgQyMDAzBDIwMDQEMjAwNQQyMDA2BDIwMDcEMjAwOAQyMDA5BDIwMTAEMjAxMQQyMDEyBDIwMTMEMjAxNAQyMDE1BDIwMTYEMjAxNwQyMDE4BDIwMTkEMjAyMAQyMDIxBDIwMjIVGAQxOTk5BDIwMDAEMjAwMQQyMDAyBDIwMDMEMjAwNAQyMDA1BDIwMDYEMjAwNwQyMDA4BDIwMDkEMjAxMAQyMDExBDIwMTIEMjAxMwQyMDE0BDIwMTUEMjAxNgQyMDE3BDIwMTgEMjAxOQQyMDIwBDIwMjEEMjAyMhQrAxhnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZAIJDxAPZBYCHwcFGE9uQ2hhbmdlRHJwQWN0UHJveSh0aGlzKWRkZAICD2QWDAINDw8WAh4HVmlzaWJsZWhkZAIPDw8WAh8IZ2RkAhUPDxYCHwhoZGQCIQ8PFgIfCGdkZAIjDw8WAh8IaGRkAj8PDxYCHwhoZGQCBA9kFgJmD2QWBgIBD2QWBGYPZBYKAgIPDxYEHgdDZWxsQXJnBQRjb2wxHgdUb29sVGlwBSVQcmVzdXB1ZXN0byBJbnN0aXR1Y2lvbmFsIGRlIEFwZXJ0dXJhZBYEZg8VAQNQSUFkAgEPZBYCAgEPFgIeDlBvcHVwQ29udHJvbElEBQZQbmxQSUFkAgMPDxYEHwkFBGNvbDIfCgUkUHJlc3VwdWVzdG8gSW5zdGl0dWNpb25hbCBNb2RpZmljYWRvZBYEZg8VAQNQSU1kAgEPZBYCAgEPFgIfCwUGUG5sUElNZAIEDw8WBB8JBQRjb2w4HwpkZBYEZg8VAQ5DZXJ0aWZpY2FjacOzbmQCAQ9kFgICAQ8WAh8LBRBQbmxDZXJ0aWZpY2FjaW9uZAIFDw8WBB8JBQRjb2wzHwpkZBYEZg8VARBDb21wcm9taXNvIEFudWFsZAIBD2QWAgIBDxYCHwsFDFBubENvbXBBbnVhbGQCBw8PFgQfCQUEY29sNx8KZGQWAmYPFQEIQXZhbmNlICVkAgEPZBYGZg8PFgQfCQUEY29sNB8KZGQWAmYPFQEfQXRlbmNpw7NuIGRlIENvbXByb21pc28gTWVuc3VhbGQCAQ8PFgQfCQUEY29sNR8KZGQWAmYPFQEJRGV2ZW5nYWRvZAICDw8WBB8JBQRjb2w2HwpkZBYCZg8VAQZHaXJhZG9kAgMPDxYCHwhnZBYCAgkPDxYCHwhoZGQCBQ8PFgIfCGhkFgICAQ88KwAHAQAPFgYeCFBhZ2VTaXplApADHgtDdXJyZW50UGFnZQIBHglJdGVtQ291bnQCGWRkAgkPDxYCHgRUZXh0BRMwNSBkZSBtYXlvIGRlIDIwMjIuZGRkZs6MvrVKuSqaXjlGgHiLbPGAo1ey68zzx1aRUsN8ru0=',
        '__EVENTVALIDATION':'/wEdACnXEL49EY6CYysQAss0OIgh5EdtbTHqfmqN1rp7Gf0xZSQ8TBsjUqNP7PZB7LXAwUxi1+RQQgFa7RCJSHKoIh8bkF9q1EGo6Oi6DTPyBDKoS9XLHxff3Ik9aTo789+FO0AfoMvnz7K3WQv+WuErvE5fNiszC6wQ5ste1/jV76Q4VvZqkrjYVtxKRHqCMZl4f7BeXYIGkvHq6nMIHcevvSVm0yWGCmhBUACBaC6uFR2XCotGnxduM3+h9gZS8BdfBruDGU89IQjdPnzsJekPA7z+gdKl+8havS5rYkzEbc/TBS6gPDGQvCN5sy0oun/v6kfQ2NgviJjarn9pF00iIc1+MsIHlJEPXUKjNdahAoyYBXn1il1SYJL8WVTNp+J8jX4StOnUp9Zq98S/oku7tbh82mhqVxaWBTExaoXx0r2v55wqaW3+pi6+Lx2mIaX4x5rngllvizktMYSvEMR8GStg0HD9YELOAQGJQqNt2ku2JdYRAr9ohmWpibcW4TTWMBxO5w7IIe25oKz1c0u0pSYn9EZv2sI13MVDhH84bT3lcEJvbtH8nSW6n8fmvBkY2Zz61Jxn+R9jfjVJerpHRoeArDZlyTyRZqbf+41nghXjjsDIMQ2ZS73du4OI0hxXEV6r9lP8KQhwOE5MAGbHRFxFtZyuB47qiJPkLre+EtbR438UByklEYO0QVYZV2PQW+vC+kK/vGnv3JqbRwMaYh6yetGtxXLOCDxqt0pk8Q5bFHYYqP1BddHzbn+N/BU4Wb1A45Iy5m48s0OxA4xoinjFYEKdrPagKHzopY90suIQyCHEhzut07raMFC8K0S2P23QzabNiRJP67fFYNfEZ4Qd7mjH5RhKFrQdBnweNNoczvE7zhbq62oAxRQwOxjbUzwEH1rcI+BIePAJGbg+m+Dc',
        
    }

    ##post request using the url , the headers and body
    response = requests.post(url, headers=headers, data=body)

    ##access the to html element of the response
    html = response.text
    ##print(html)
    soup = BeautifulSoup(html, 'html.parser')
    fechaActualizacion=soup.find(id="ctl00_CPH1_LblLastUpdate").text

    ##print('***************')
    print(fechaActualizacion)
    print('***************')
    ##print('***************')
    table  = soup.find_all('table', { "class" : "Data"})
    ##print(table)

    #Count tr in table
    tr_count = len(table[0].find_all('tr'))    
    print('tr_count')
    print(tr_count)#Result: tr_count = 800, 400 groups of 2 rows...from id="tr0" to id="tr399"
    tr_count_group=(tr_count/2)

    #select tr by id="tr0" in table
    tr = table[0].find_all('tr', id="tr0")
    #print(tr)
    #tr_count_group-1
    for i in range(0, 5):
        idtext="tr"+str(i)
        row=table[0].find_all('tr', id=idtext)
        obtainColsFromRows(row[0])
        #print(tr)  
    #Contain <tr id="tr0" onclick='kCod="2000032"
    zero_row = table[0].find_all('tr')[0]

    ##extract first row of the table Contain NONE
    first_row = table[0].find_all('tr')[1]
    ##extract each column of the row
    first_row_cols = first_row.find_all('td')
    #print(first_row)

    ##extract second row of the table
    ##Contain .....Data.....
    """
    <tr class="alt" id="tr1" onclick='kCod="2000055";tr_clk(1, this)'
								onmouseover="tr_over(this)" onmouseout="tr_out(this)">
								<td id="ctl00_CPH1_RptData_ctl02_TD0" align="center" valign="top" rowspan="2">
									<input type="radio" name="grp1" value="2000055/1329238/942526/79666.10/79666.10/79666.10/79666.10/79666.10"
                                        onclick='kCod = "2000055    ";grp1_clk(1)'>
                                </td>

								<td align="left">
									2000055: MEJORAMIENTO DE PARQUES

								</td>
								<td>
									1,329,238
								</td>
								<td>
									942,526
								</td>
								<td>
									79,666
								</td>
								<td>
									79,666
								</td>
								<td>
									79,666
								</td>
								<td>
									79,666
								</td>
								<td>
									79,666
								</td>
								<td>&nbsp;
									8.5
								</td>
							</tr>
    """
    second_row = table[0].find_all('tr')[2]
    ##print(second_row)
    #extract each column of the second_row
    second_row_cols = second_row.find_all('td')
    #print(second_row_cols)
    """
    <td align="center" id="ctl00_CPH1_RptData_ctl02_TD0" rowspan="2" valign="top">
<input name="grp1" onclick='kCod = "2000055    ";grp1_clk(1)' type="radio" value="2000055/1329238/942526/79666.10/79666.10/79666.10/79666.10/79666.10"/>
</td>, <td align="left">
                                    2000055: MEJORAMIENTO DE PARQUES

                                </td>, <td>
                                    1,329,238
                                </td>, <td>
                                    942,526
                                </td>, <td>
                                    79,666
                                </td>, <td>
                                    79,666
                                </td>, <td>
                                    79,666
                                </td>, <td>
                                    79,666
                                </td>, <td>
                                    79,666
                                </td>, <td> 
                                    8.5
                                </td>
    """

    
    """
    ##print('***************')
    #extract each column of the second_row text values
    counter = 0
    codigoDNPP=""
    nombreDNPP=""

    pIA=""
    pIM=""    
    certificacion=""
    compromisoAnual=""
    compromisoMensual=""
    devengado =""
    girado =""
    avancePercent=""
    for col in second_row_cols:
        #note 
        #if counter == 0: , palabraEditada return ' '

        #replace break line with space in col.text
        palabra=col.text
        palabraEditada = palabra.replace('\n', ' ') 

        #only for the first column, split by ':'        
        if counter==1:
            x = palabraEditada.split(": ")
            codigoDNPP=x[0]
            nombreDNPP=x[1]
            #print(x)
        if counter==2:
            pIA=palabraEditada
            
        if counter==3:
            pIM=palabraEditada    
        if counter==4:              
            certificacion=palabraEditada
        if counter==5:            
            compromisoAnual=palabraEditada            
        if counter==6:            
            compromisoMensual=palabraEditada            
        if counter==7:            
            devengado=palabraEditada
        if counter==8:            
            girado=palabraEditada
        if counter==9:            
            avancePercent=palabraEditada
       
        counter+=1

    
        print(palabraEditada)
    print('***************')
    print(codigoDNPP)
    print(nombreDNPP.replace('\r', '') )
    print(pIA)
    print(pIM)
    print(certificacion)
    print(compromisoAnual)
    print(compromisoMensual)
    print(devengado)
    print(girado)
    print(avancePercent)
    """

    """ 
    ##extract each row of the table
    for row in table[0].find_all('tr'):
        ##extract each column of the row
        for col in row.find_all('td'):
            print(col.text)
    ### 
    """

def obtainColsFromRows(row):
    #second_row = table[0].find_all('tr')[2]
    second_row=row
    ##print(second_row)
    #extract each column of the second_row
    second_row_cols = second_row.find_all('td')
    #print(second_row_cols)
    """
    <td align="center" id="ctl00_CPH1_RptData_ctl02_TD0" rowspan="2" valign="top">
<input name="grp1" onclick='kCod = "2000055    ";grp1_clk(1)' type="radio" value="2000055/1329238/942526/79666.10/79666.10/79666.10/79666.10/79666.10"/>
</td>, <td align="left">
                                    2000055: MEJORAMIENTO DE PARQUES

                                </td>, <td>
                                    1,329,238
                                </td>, <td>
                                    942,526
                                </td>, <td>
                                    79,666
                                </td>, <td>
                                    79,666
                                </td>, <td>
                                    79,666
                                </td>, <td>
                                    79,666
                                </td>, <td>
                                    79,666
                                </td>, <td> 
                                    8.5
                                </td>
    """

    
    ##print('***************')
    #extract each column of the second_row text values
    counter = 0
    codigoDNPP=""
    nombreDNPP=""

    pIA=""
    pIM=""    
    certificacion=""
    compromisoAnual=""
    compromisoMensual=""
    devengado =""
    girado =""
    avancePercent=""

    linkToFichaProyecto=r"https://apps5.mineco.gob.pe/transparencia/Reportes/RptFichaProy.aspx?y=2022&ap="
    #https://apps5.mineco.gob.pe/transparencia/Reportes/RptFichaProy.aspx?y=2022&ap=2000032
    for col in second_row_cols:
        #note 
        #if counter == 0: , palabraEditada return ' '

        #replace break line with space in col.text
        palabra=col.text
        palabraEditada = palabra.replace('\n', ' ') 

        #only for the first column, split by ':'        
        if counter==1:
            x = palabraEditada.split(": ")
            codigoDNPP=x[0]
            nombreDNPP=x[1]
            #print(x)
        if counter==2:
            pIA=palabraEditada
            
        if counter==3:
            pIM=palabraEditada    
        if counter==4:              
            certificacion=palabraEditada
        if counter==5:            
            compromisoAnual=palabraEditada            
        if counter==6:            
            compromisoMensual=palabraEditada            
        if counter==7:            
            devengado=palabraEditada
        if counter==8:            
            girado=palabraEditada
        if counter==9:            
            avancePercent=palabraEditada
        """
        if counter==2:
            pIA=palabraEditada
            pIM=palabraEditada    
            certificacion=palabraEditada
            compromisoAnual=palabraEditada
            compromisoMensual=palabraEditada
            devengado =palabraEditada
            girado=palabraEditada
            avancePercent=palabraEditada
        """
        counter+=1

    
        print(palabraEditada)
    linkToFichaProyecto=linkToFichaProyecto+str(codigoDNPP)
    print('***************')
    print(codigoDNPP)
    print(nombreDNPP.replace('\r', '') )
    print(pIA)
    print(pIM)
    print(certificacion)
    print(compromisoAnual)
    print(compromisoMensual)
    print(devengado)
    print(girado)
    print(avancePercent)
    print(linkToFichaProyecto)

scrapper('https://apps5.mineco.gob.pe/transparencia/Navegador/Navegar_7.aspx')

    


