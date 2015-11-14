
function plotCPU(){
	var cpuX = [];
	var cpuY = [];
	var secondsPast = 0;
	var read = 0;
	
	drawPlot();

	function drawPlot(){	
		
		read += 1;
		if(read > 80) {
			read -= 30;
		} else if (read < 0) {
			read = 0;
		}
		secondsPast += 1;
		cpuX.push([secondsPast, read+10]);
		cpuY.push([secondsPast, 70]);
		
		if (cpuX.length > 60){
			
			cpuX.shift();
			cpuY.shift();
		}
		
	$.plot($("#cpu"), [cpuX,cpuY], {
	    grid: {
	        borderWidth: 1,
	        minBorderMargin: 5,
	        labelMargin: 2,
	        // backgroundColor: {
	        //     colors: ["#fff", "#e4f4f4"]
	        // }//,
	        margin: {
	            top: 1,
	            bottom: 5,
	            left: 2
	        }
	    },
	    yaxis: {
	        labelWidth: 30,
			max:100
	    },
	    xaxis: {
	        labelHeight: 30,
	    },
	    legend: {
	        show: true
	    },
		colors:["green","red"]
	});
	// defining the style of axis and their coordinate labels
	var xaxisLabel = $("<div class='axisLabel xaxisLabel'></div>").text("Elapsed Time").appendTo($('#cpu'));
	var yaxisLabel = $("<div class='axisLabel yaxisLabel'></div>").text("Percentage").appendTo($('#cpu'));
	yaxisLabel.css("margin-top", yaxisLabel.width() / 2 - 20);
	setTimeout(drawPlot, 1000);
}


