$("#pause").click(function(e) {
      e.preventDefault();

      $.ajax({
        url: "http://127.0.0.1:8000/music/pause/",
        type: "GET",
        data:{},
        success: function(response) {
        },
        error: function (xhr, errmsg, err) {
        }
      });
      $("#pause")[0].hidden = true;
      $("#unpause")[0].hidden = false;
    });


$("#unpause").click(function(e) {
      e.preventDefault();
      console.log("Unpaused");
      $.ajax({
        url: "http://127.0.0.1:8000/music/unpause/",
        type: "GET",
        data:{},
        success: function(response) {
        },
        error: function (xhr, errmsg, err) {
        }
      });
      $("#unpause")[0].hidden = true;
      $("#pause")[0].hidden = false;
    });


$("#next").click(function(e) {
      e.preventDefault();
      console.log("Unpaused");
      $.ajax({
        url: "http://127.0.0.1:8000/music/nextsong/",
        type: "GET",
        data:{},
        success: function(response) {
        },
        error: function (xhr, errmsg, err) {
        }
      });
      $("#unpause")[0].hidden = true;
      $("#pause")[0].hidden = false;
    });


$("#previous").click(function(e) {
      e.preventDefault();
      console.log("Unpaused");
      $.ajax({
        url: "http://127.0.0.1:8000/music/prevsong/",
        type: "GET",
        data:{},
        success: function(response) {
        },
        error: function (xhr, errmsg, err) {
        }
      });
      $("#unpause")[0].hidden = true;
      $("#pause")[0].hidden = false;
    });
