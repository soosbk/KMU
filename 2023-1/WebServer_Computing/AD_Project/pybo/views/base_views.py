from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count(
            'answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page,
               'kw': kw, 'so': so}  # <------ so 추가
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # 입력 파라미터
    comments_page = request.GET.get('comments_page', '1')  # 댓글 페이지
    comments_so = request.GET.get('comments_so', 'recent')  # 댓글 정렬기준

    # 정렬
    if comments_so == 'recommend':
        question_comments = question.comment_set.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    else:  # recent
        question_comments = question.comment_set.order_by('-create_date')

    # 댓글 페이징처리
    question_comments_paginator = Paginator(
        question_comments, 5)  # 페이지당 5개씩 보여주기
    question_comments_page_obj = question_comments_paginator.get_page(
        comments_page)

    
   
    context = {
        'question': question,
        'question_comments_page_obj': question_comments_page_obj,
        'comments_page': comments_page,
        'comments_so': comments_so,
    }
    return render(request, 'pybo/question_detail.html', context)
