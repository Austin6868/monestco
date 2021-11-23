from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from monest.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view,permission_classes
from django.http import JsonResponse
from monest.models import Company,Scores, Facts, News, Industry, IndustryStandards
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# API refactoring(After database refactoring)
# stage 1:  migrate old APIs, keep everything unchanged(URLs, names, params, methods..etc)
# Stage 2: optimized APIs, subject them to best practices(require frond-end API call change accordingly)
# API Optimization directions:
#   1. remove inappropriate use of POST method
#   2. better URL design
#   3. remove redundant APIs(e.g. similarCompany1/2/3/4)
#   4. remove unnecessary params and return payload
#   5. exception handling


@permission_classes([IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@permission_classes([IsAuthenticated])
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    """
    Serve the frontend from here
    frond end is an React App
    Home Page
    the frond end path has already added in setting.py
    """
    return render(request, "index.html")


@api_view(['GET'])
def all_company_names(request):
    """
    Get all companies
    """
    companies = Company.objects.values_list('name', flat=True)
    data = []
    for item in companies:
        data.append({
            "Name": item
        })
    return JsonResponse({
        'rows': data
    }, safe=False)


@api_view(['GET'])
def companies(request, company=''):
    return JsonResponse([], safe=False
                        )


@csrf_exempt
@api_view(['GET', 'POST'])
def company_scores(request):
    company_name = request.query_params['0']
    company = Company.objects.get(name=company_name)
    scores = Scores.objects.all().filter(company=company)
    res = {}
    for item in scores:
        score_key = item.metric.types + 'score'
        res[score_key] = item.score
        if item.short_text:
            short_key = item.metric.types + 'short'
            long_key = item.metric.types + 'long'
            res[short_key] = item.short_text
            res[long_key] = item.long_text

    return JsonResponse([res], safe=False
                        )


@api_view(['GET', 'POST'])
def a_scores(request):
    company_name = request.query_params['0']
    company = Company.objects.get(name=company_name)
    scores = Scores.objects.all().filter(company=company, metric__types__contains='A')
    res = {}
    for item in scores:
        score_key = item.metric.types + 'score'
        res[score_key] = item.score
        if item.short_text:
            short_key = item.metric.types + 'short'
            long_key = item.metric.types + 'long'
            res[short_key] = item.short_text
            res[long_key] = item.long_text

    return JsonResponse({
        'rows': [res]
    }, safe=False)


@api_view(['GET', 'POST'])
def b_scores(request):
    company_name = request.query_params['0']
    company = Company.objects.get(name=company_name)
    scores = Scores.objects.all().filter(company=company, metric__types__contains='B')
    res = {}
    for item in scores:
        score_key = item.metric.types + 'score'
        res[score_key] = item.score
        if item.short_text:
            short_key = item.metric.types + 'short'
            long_key = item.metric.types + 'long'
            res[short_key] = item.short_text
            res[long_key] = item.long_text

    return JsonResponse({
        'rows': [res]
    }, safe=False)


@api_view(['GET', 'POST'])
def c_scores(request):
    company_name = request.query_params['0']
    company = Company.objects.get(name=company_name)
    scores = Scores.objects.all().filter(company=company, metric__types__contains='C')
    res = {}
    for item in scores:
        score_key = item.metric.types + 'score'
        res[score_key] = item.score
        if item.short_text:
            short_key = item.metric.types + 'short'
            long_key = item.metric.types + 'long'
            res[short_key] = item.short_text
            res[long_key] = item.long_text

    return JsonResponse({
        'rows': [res]
    }, safe=False)


@api_view(['GET', 'POST'])
def d_scores(request):
    company_name = request.query_params['0']
    company = Company.objects.get(name=company_name)
    scores = Scores.objects.all().filter(company=company, metric__types__contains='D')
    res = {}
    for item in scores:
        score_key = item.metric.types + 'score'
        res[score_key] = item.score
        if item.short_text:
            short_key = item.metric.types + 'short'
            long_key = item.metric.types + 'long'
            res[short_key] = item.short_text
            res[long_key] = item.long_text

    return JsonResponse({
        'rows': [res]
    }, safe=False)

@api_view(['GET', 'POST'])
def score_citations(request):
    company_name = request.query_params['0']
    company = Company.objects.get(name=company_name)
    scores = Scores.objects.all().filter(company=company)
    res = []
    for score in scores:
        citations = score.citation.all()
        for item in citations:
            res.append({
                'ID': item.id,
                'Type': score.metric.types,
                'Author': item.author,
                'Title': item.title,
                'PublishingGroup': item.publisher,
                'Date': item.date,
                'Pages': item.pages,
                'URL': item.url
            })
    return JsonResponse(res, safe=False)


@api_view(['GET', 'POST'])
def other_company_info(request):
    company_name = request.query_params['0']
    company = Company.objects.get(name=company_name)
    scores = Scores.objects.all().filter(company=company, metric__types__in=['A', 'B', 'C', 'D'])
    total_score = 0
    for item in scores:
        total_score += item.score
    total_score = round(total_score/4)
    res = {}
    res['Logo'] = company.logo
    res['Subsidiary'] = company.parent_company
    res['TotalScore'] = total_score

    return JsonResponse([res], safe=False)


@api_view(['GET', 'POST'])
def company_name(request):
    company_name = request.query_params['0']
    company = Company.objects.get(name=company_name)
    res = {}
    res['Name'] = company.name
    if company.parent_company:
        res['Subsidiary'] = company.parent_company
    else:
        res['Subsidiary'] = None
    res['Category'] = company.category
    res['Description'] = company.description
    res['Logo'] = company.logo
    res['SimilarCompany1'] = company.similar_company_1
    res['SimilarCompany2'] = company.similar_company_2
    res['SimilarCompany3'] = company.similar_company_3
    res['SimilarCompany4'] = company.similar_company_4
    scores = Scores.objects.all().filter(company=company, metric__types__in=['A', 'B', 'C', 'D'])
    total_score = 0
    for item in scores:
        total_score += item.score
    res['TotalScore'] = round(total_score/4)

    return JsonResponse([res], safe=False)


@api_view(['GET', 'POST'])
def facts(request):
    company_name = request.query_params['0']
    company = Company.objects.get(name=company_name)
    fact_items = Facts.objects.all().filter(company=company)
    res = []
    for item in fact_items:
        res.append({
            'ID': item.id,
            'Heading': item.heading,
            'Summary': item.summary
        })

    return JsonResponse(res, safe=False)


@api_view(['GET', 'POST'])
def fact_citations(request):
    fact_id = request.query_params['1']
    citations = Facts.objects.get(id=fact_id).citation.all()
    res = []
    for item in citations:
        res.append({
            'ID': item.id,
            'Author': item.author,
            'Title': item.title,
            'PublishingGroup': item.publisher,
            'Date': item.date,
            'Pages': item.pages,
            'URL': item.url
        })
    return JsonResponse(res, safe=False)


@api_view(['GET', 'POST'])
def news(request):
    company_name = request.query_params['0']
    company = Company.objects.get(name=company_name)
    news_items = News.objects.all().filter(company=company)
    res = []
    for item in news_items:
        res.append({
            'ID': item.id,
            'Photo': item.photo,
            'Year': item.year,
            'Category': item.category,
            'Title': item.title,
            'Summary': item.summary,
            'IssueAddressed': item.issue_addressed,
            'IssueAddressedExplanation': item.issue_addressed_text,
            'ResponsibilityTaken': item.responsibility_taken,
            'ResponsibilityTakenExplanation': item.responsibility_taken_text
        })

    return JsonResponse(res, safe=False)


@api_view(['GET', 'POST'])
def news_citations(request):
    news_id = request.query_params['1']
    citations = News.objects.get(id= news_id).citation.all()
    res = []
    for item in citations:
        res.append({
            'ID': item.id,
            'Author': item.author,
            'Title': item.title,
            'PublishingGroup': item.publisher,
            'Date': item.date,
            'Pages': item.pages,
            'URL': item.url
        })
    return JsonResponse(res, safe=False)

def get_company_score(name: str) -> {}:
    company = Company.objects.get(name=name)
    scores = Scores.objects.all().filter(company=company, metric__types__in=['A', 'B', 'C', 'D'])
    res = {}
    for item in scores:
        if item.metric.types == 'A':
            res['Ascore'] = item.score
        elif item.metric.types == 'B':
            res['Bscore'] = item.score
        elif item.metric.types == 'C':
            res['Cscore'] = item.score
        elif item.metric.types == 'D':
            res['Dscore'] = item.score

    return res


@api_view(['GET', 'POST'])
def similar_company_1(request):
    try:
        company_name = request.query_params['0']
        company = Company.objects.get(name=company_name)
        res = get_company_score(company.similar_company_1)
        return JsonResponse([res], safe=False)
    except Company.DoesNotExist:
        return JsonResponse([{
            'Ascore': 0,
            'Bscore': 0,
            'Cscore': 0,
            'Dscore': 0
        }], safe=False)


@api_view(['GET', 'POST'])
def similar_company_2(request):
    try:
        company_name = request.query_params['0']
        company = Company.objects.get(name=company_name)
        res = get_company_score(company.similar_company_2)
        return JsonResponse([res], safe=False)
    except Company.DoesNotExist:
        return JsonResponse([{
            'Ascore': 0,
            'Bscore': 0,
            'Cscore': 0,
            'Dscore': 0
        }], safe=False)

@api_view(['GET', 'POST'])
def similar_company_3(request):
    try:
        company_name = request.query_params['0']
        company = Company.objects.get(name=company_name)
        res = get_company_score(company.similar_company_3)
        return JsonResponse([res], safe=False)
    except Company.DoesNotExist:
        return JsonResponse([{
            'Ascore': 0,
            'Bscore': 0,
            'Cscore': 0,
            'Dscore': 0
        }], safe=False)


@api_view(['GET', 'POST'])
def similar_company_4(request):
    try:
        company_name = request.query_params['0']
        company = Company.objects.get(name=company_name)
        res = get_company_score(company.similar_company_4)
        return JsonResponse([res], safe=False)
    except Company.DoesNotExist:
        return JsonResponse([{
            'Ascore': 0,
            'Bscore': 0,
            'Cscore': 0,
            'Dscore': 0
        }], safe=False)


@api_view(['GET', 'POST'])
def industry_standards(request):
    """
    current implementation in Nodejs is hardcoded return Apparel.
    Need Optimization in stage 2
    :param request:
    :return:
    """
    standards = IndustryStandards.objects.all().filter(industry='Apparel')
    res = {}
    for item in standards:
        total_key = item.metric.types + 'total'
        low_key = item.metric.types + 'low'
        high_key = item.metric.types + 'high'
        res[total_key] = item.total
        res[low_key] = item.low
        res[high_key] = item.high

    return JsonResponse({
        'rows': [res]
        }, safe=False)


