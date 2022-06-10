
$(function(){
  $('.filter_all').click(function(event){
    $('.kor').show();
    $('.cn').show();
    $('.jp').show();
    $('.us').show();
  })
  $('.filter_kor').click(function(event){
    $('.kor').show();
    $('.cn').hide();
    $('.jp').hide();
    $('.us').hide();
  })
  $('.filter_cn').click(function(event){
    $('.cn').show();
    $('.kor').hide();
    $('.jp').hide();
    $('.us').hide();
  })
  $('.filter_jp').click(function(event){
    $('.jp').show();
    $('.kor').hide();
    $('.cn').hide();
    $('.us').hide();
  })
  $('.filter_us').click(function(event){
    $('.us').show();
    $('.kor').hide();
    $('.cn').hide();
    $('.jp').hide();
  })

  $('.wBtn').click(function(){
    if($(this).hasClass('active')){
      $('.wBtn').removeClass('active');
    }else{
      $('.wBtn').removeClass('active');
      $(this).addClass('active')
    }
  })

  // 모달창 관련
  var open=$('#modal_opne_btn');
  var close=$('#modal_close_btn');
  var content=$('.booking');

  content.hide();
  open.click(function(){
    content.show();
  })
  close.click(function(){
    content.hide();
  })

  // 스킬바 관련
  function animated_contents() {
    $(".zt-skill-bar > div ").each(function (i) {
      var $this  = $(this),
      skills = $this.data('width');

      $this.css({'width' : skills + '%'});

    });
  }
  
  if(jQuery().appear) {
    $('.zt-skill-bar').appear().on('appear', function() {
      animated_contents();
    });
  } else {
    animated_contents();
  }
  $('#waypoint').waypoint(function(){
    $('#waypoint').addClass('animate__fadeIn');
  }, {offset: '83%'});

  var top5=$('.top5')
  var top4=$('.top4')
  var top3=$('.top3')
  var top2=$('.top2')
  var top1=$('.top1')

  var top5_1=$('.top5-1')
  var top4_1=$('.top4-1')
  var top3_1=$('.top3-1')
  var top2_1=$('.top2-1')
  var top1_1=$('.top1-1')

  var hide=$('.hide')

  top5.click(function(event){
    top5_1.toggle();
    top4_1.hide();
    top3_1.hide();
    top2_1.hide();
    top1_1.hide();
  })

  top4.click(function(event){
    top4_1.toggle();
    top5_1.hide();
    top3_1.hide();
    top2_1.hide();
    top1_1.hide();
  })

  top3.click(function(event){
    top3_1.toggle();
    top5_1.hide();
    top4_1.hide();
    top2_1.hide();
    top1_1.hide();
  })

  top2.click(function(event){
    top2_1.toggle();
    top5_1.hide();
    top4_1.hide();
    top3_1.hide();
    top1_1.hide();
  })

  top1.click(function(event){
    top1_1.toggle();
    top5_1.hide();
    top4_1.hide();
    top3_1.hide();
    top2_1.hide();
  })

})
