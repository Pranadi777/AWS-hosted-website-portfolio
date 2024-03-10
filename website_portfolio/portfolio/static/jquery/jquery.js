

  $(".item").on("click", (e) => {

      var element = document.getElementById('projects');
      element.scrollIntoView({
        block: 'start',
        behavior: 'smooth',
      });

  });
