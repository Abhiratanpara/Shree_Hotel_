let navBar =document.querySelectorAll(".nav-link");
let navcollapse =document.querySelector(".navbar-collapse.collapse");
navBar.forEach(function(a){
  a.addEventListener("click",function(){
    navcollapse.classList.remove("show");
  })
});

var swiper = new Swiper('.mySwiper', {
    // Optional parameters
    direction: 'vertical',
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
      clickable:true,
    },

    autoplay:{
        delay:3500,
    },
  

  });

  document.addEventListener("DOMContentLoaded",() =>{
    function counter(id,start,end,duration) {
      let obj = document.getElementById(id),
      current=start,
      range=end-start,
      increment=end > start ? 1 : -1,
      step=Math.abs(Math.floor(duration/range)),
      timer=setInterval(() => {
        current += increment;
        obj.textContent =current;
        if(current == end){
          clearInterval(timer);
        }
      },step);
    }
    counter("count1", 0, 150, 3000);
    counter("count2", 1500, 2000, 500);
    counter("count3", 100, 500, 3000);
    counter("count4", 50, 200, 3000);
  })
  