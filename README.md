<h2>Pandas introduction</h2>
<pre>
판다스(Pandas)라는 모듈은 1차원 데이터를 다루는 Series 타입과 2차원 데이터를 위한 DataFrame 타입을 제공합니다.
</pre>

<h2>Series</h2>
<pre>
- 단순하게 리스트를 저장하는 딕셔러니라고 생각하면된다.
- Series(값, index=인덱스) 로 지정하면된다.
- 인덱스를 명시하지 않으면 정수 0부터 시작하여 순번이 매겨지고, 
  인덱스를 명시하면 순번이 보이지는 않지만 순번이 똑같이 저장된다. 
- 따라서 슬라이싱과 인덱싱을 할때 인덱스를 사용해도 되고 순번을 사용해도된다.
- 삭제는 drop()함수를 사용한다.
- 리스트와 다르게 사측연산도 가능하다.
</pre>

<h2>DataFrame</h2>
<pre>
DataFrame은 2차원데이터, 즉 진짜 표를 만드는 것이다.
자동 생성된 번호 대신 다른 Column을 index로 지정하기 위해서는 
set_index 함수를 사용합니다.
pandas 모듈의 read_html() 함수는 웹페이지를 DataFrame으로 변환합니다
</pre>