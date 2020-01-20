from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return render(request,'base2.html')

def analyze(request):
    rawtext=request.POST.get('rawtext','notext')
    rp=request.POST.get('rp','notext')
    sr=request.POST.get('sr','notext')
    esr=request.POST.get('esr','notext')
    up=request.POST.get('up','notext')
    lo=request.POST.get('lo','notext')
    nlr=request.POST.get('nlr','notext')
    cc=request.POST.get('cc','notext')

    count=0
    if cc=='on':
        count=len(rawtext)
    if up=='on':
        rawtext=rawtext.upper()
    if lo=='on':
        rawtext=rawtext.lower()
    if rp=='on':
        newtext=''
        punc='~!@#$%^&*()_+-=`,.<>:";'
        for l in rawtext:
            if l not in punc:
                newtext=newtext+l
        rawtext=newtext
    if sr=='on':
        newtext=''
        for l in rawtext:
            if l not in [' ']:
                newtext+=l
        rawtext=newtext
    if esr=='on':
        newtext=''
        for i in range(len(rawtext)-1):
                if rawtext[i]==' ' and rawtext[i+1]==' ':
                    pass
                else:
                    newtext+=rawtext[i]
        newtext += rawtext[i+1]
        rawtext=newtext
    if nlr == 'on':
        newtext = ''
        for l in rawtext:
            if l !="\n" and l!="\r":
                newtext += l
        rawtext = newtext



    params={ 'rawtext':rawtext,'cc':count}
    return render(request,'next2.html',params)
