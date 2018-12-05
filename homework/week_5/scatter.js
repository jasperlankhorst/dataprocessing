// Jasper Lankhorst
// 10885803
// Makes a scatter plot for week 5

window.onload = function() {

  console.log('Yes, you can!')
};

window.onload = function() {
  $.getJSON("https://data.mprog.nl/course/10%20Homework/100%20D3%20Scatterplot/datasets/msti.json",
    function(data) {


// svg aanmaken

      var svg = d3.select("body").append("svg")
                                 .attr("width", 200)
                                 .attr("height", 200);

// cirkels

      var circles = svg.selectAll("circle")
                     .data(root)
                     .enter()
                     .append("circle")
                     .attr("y", function(root) {
                       var y = 
                       return y
                     })
                     // .attr("width", 10)
                     // .attr("height", function(root) {
                     //   return root["value"];
                     // })
                     // .attr("fill", "rgb(200,200,200)")
                     // .attr("transform", function(root,i) {
                     //   var translate = [];
                     //   return "translate(" + translate + ")";
                     });
         });
    });

};
