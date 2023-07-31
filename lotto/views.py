from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.



def index(request):

    # request.POST - > dict
    #
    # - dict의 key == input tag의 name 값
    # - dict의 value == input tag의 value 값(== USER의 입력값)
    #
    # request.POST['fname'] - > '안녕하세요.'
    # request.POST['lname'] - > '반갑습니다.'

    lottos = GuessNumbers.objects.all()

    return render(request, 'lotto/default.html' , {'lottos':lottos}) # context-dict


def post(request):

    if request.method == 'POST' : # POST 요청이 들어온 경우

        form = PostForm(request.POST)

        if form.is_valid():

            lotto = form.save(commit=False)
            lotto.generate()
            # lotto.save()

            return redirect('index')

            # return render(request, '~~~/~~~.html', {})


            # lotto.text = lotto.text.upper()
            # lotto.lottos = '[1, 10, 20, 30, 9, 5]'
            # lotto.save()

            # new_row = GuessNumbers()
            # new_row.text = new_row.text.upper()
            # new_row.save(commit=False)


        # form.save()

        # print('\n\n\n')
        # print(request.POST) # 'GET', 'POST'
        # print(type(lotto)) # <class 'lotto.models.GuessNumbers'>

        #  print(type(form)) #<class 'lotto.forms.PostForm'>
        # print(lotto) # pk None : 테스트입니다 - 안녕하세요

        # print(request.POST['csrfmiddlewaretoken'])
        # print(request.POST['name'])
        # print(request.POST['text'])

        # print('\n\n\n')


    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})


def hello(request):
    # data = GuessNumbers.objects.all()
    # data = GuessNumbers.objects.get(id=1)

    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

    # index.html
    # <input type='text' name='name' ></input>    <- #'win the prize!'
    # <input type='text' name='text' ></input>
    # USER가 값을 입력하고 ,전송 버튼을 클릭 -> USER가 입력한 값을 가지고 HTTP POST request


    # user_input_name = request.POST['name'] # HTML 에서 name이 'name'인 input tag에 대해 USER가 입력한 값
    # user_input_text = request.POST['text'] # HTML 에서 input tag 의 name이 'text'인 input tag에 대해 USER가 입력한 값
    #
    # new_row = GuessNumbers(name=user_input_name, text=user_input_text)
    #
    # print(new_row.num_lotte) # 5
    # print(new_row.name) # 'win the prize!'
    #
    # new_row.name = new_row.name.upper() # 'WIN THE PRIZE!'
    # new_row.lottos = [ np.randint(1, 50) for i in range(6) ]
    #
    # new_row.save()

    # request.POST['name']

    return render(request, 'lotto/default.html' , {})


def hello(request):

    # data = GuessNumbers.objects.all()
    # data = GuessNumbers.objects.get(id=1)

    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")


def detail(request, lottokey):

    lotto = GuessNumbers.objects.get(id=lottokey)

    return render(request, 'lotto/detail.html', {'lotto':lotto})
