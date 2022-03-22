from django.shortcuts import render
from django.forms import ModelForm

from election.models import LGA, AgentName, AnnouncedPuResults, Party, PollingUnit

# Create your views here.


class PuResultsForm(ModelForm):
    class Meta:
        model = AnnouncedPuResults
        fields = '__all__'


def home(request):
    template_name = 'home.html'
    return_query = {'polling_unit': '', 'result': ''}

    if request.method == "POST":
        q = request.POST['unitid']
        unit = PollingUnit.objects.get(polling_unit_number=q)
        parties = Party.objects.all()
        results = {}
        for party in parties:
            results[party.partynmae] = 0

        if unit:
            result = AnnouncedPuResults.objects.filter(
                polling_unit_uniqueid=unit.polling_unit_id)
            for i in result:
                results[i.party_abbreviation] += i.party_score

            return_query = {'polling_unit': unit, 'result': results}

        return render(request, template_name, return_query)

    return render(request, template_name)


def lga(request):
    template_name = 'lga.html'
    lgas = LGA.objects.all()
    context = {'lgas': lgas}
    results = {}
    context['results'] = results
    parties = Party.objects.all()
    for party in parties:
        results[party.partynmae] = 0

    if request.method == 'POST':
        lga_name = request.POST['lga']
        try:
            lga = LGA.objects.get(lga_name=lga_name)
            if lga:
                context['lga'] = lga
                lga_polling_units = PollingUnit.objects.filter(
                    lga_id=lga.lga_id)
                # print(lga_polling_units)

                for polling_unit in lga_polling_units:
                    res = AnnouncedPuResults.objects.filter(
                        polling_unit_uniqueid=polling_unit.polling_unit_id)
                    print('============')
                    print(res)
                    print('============')

                    for i in res:
                        # print(i)
                        results[i.party_abbreviation] = results[i.party_abbreviation] + i.party_score
                    # context['results'] = results

            else:
                context['lga'] = ['LGA not found']
        except:
            pass

        return render(request, template_name, context)
    # return
    return render(request, template_name, context)


def addpage(request):
    template_name = 'addpage.html'
    parties = Party.objects.all()

    if request.method == 'POST':
        for party in parties:
            AnnouncedPuResults.objects.create(
                polling_unit_uniqueid=request.POST['polling_id'],
                entered_by_user=request.POST['user'],
                user_ip_address=request.POST['ip'],
                party_abbreviation=party.partyid,
                party_score=int(request.POST[party.partyid])
            )
            print(request.POST)
    return render(request, template_name, {'parties': parties})
