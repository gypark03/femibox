// JavaScript Document
function join_btn(){
	//라디오 버튼 Name 가져오기
        var ch_btn = document.getElementsByName("choice1");
 
        //라디오 버튼이 체크되었나 확인하기 위한 변수
        var ch_btn_check = 0;
        for(var i = 0; i<ch_btn.length; i++){
            //만약 라디오 버튼이 체크가 되어있다면 true
            if(ch_btn[i].checked==true){
            }
        }
        if(ch_btn_check<1){
            alert("라디오 버튼을 선택해주세요");
			document.formname.ch_btn[0].focus();
            return;
        }
}