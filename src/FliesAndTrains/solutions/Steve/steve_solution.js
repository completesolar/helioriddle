function superFly(distance_miles, train1_mph, train2_mph, fly_mph) {
		  var result = "Not sure how to answer that.";
		  if (fly_mph < train1_mph || fly_mph < train2_mph) {
		    result = "The fly is too slow!";
		  } else {
		    var total_train_mph = (train1_mph + train2_mph);
		    if (total_train_mph <= 0) {
		      result = "The trains will never collide!";
		    } else {
		      var total_time = (distance_miles/total_train_mph);
		      var fly_distance = fly_mph * total_time;
		      result = (isNaN(fly_distance)) ? result : "The fly travels " + fly_distance.toFixed(2) + " total miles.";
		    }
		  }
		  return result;
		}
		var initUnitTests = function() {
			QUnit.test( "hello test", function( assert ) {
	  			assert.ok( 1 == "1", "Passed!" );
			});
			QUnit.test("superFly test: all values legal", function(assert) {
				assert.ok(superFly(120,60,60,100) == "The fly travels 100.00 total miles.", "Happy path confirmed!");
			});
			QUnit.test("superFly test: distance illegal", function(assert) {
				assert.ok(superFly("foo",60,60,100) == "Not sure how to answer that.", "String input successfully handled.");
			});
			QUnit.test("superFly test: trainA illegal", function(assert) {
				assert.ok(superFly(120,"foo",60,100) == "Not sure how to answer that.", "String input successfully handled.");
			});
			QUnit.test("superFly test:trainB illegal", function(assert) {
				assert.ok(superFly(120,60,"foo",100) == "Not sure how to answer that.", "String input successfully handled.");
			});
			QUnit.test("superFly test: fly illegal", function(assert) {
				assert.ok(superFly(120,60,60,"foo") == "Not sure how to answer that.", "String input successfully handled.");
			});
			QUnit.test("superFly test: fly speed < train speed", function(assert) {
				assert.ok(superFly(120,60,60,59) == "The fly is too slow!", "String input successfully handled.");
			});
			QUnit.test("superFly test: train speed <= 0", function(assert) {
				assert.ok(superFly(120,60,-60,61) == "The trains will never collide!", "Train speed input successfully handled.");
			});
			QUnit.test("superFly test: train speed <= 0", function(assert) {
				assert.ok(superFly(120,60,-61,61) == "The trains will never collide!", "Train speed input successfully handled.");
			});
		}
		initUnitTests();


		document.getElementById("submit-btn").onclick = function(e) {
			var d = document.getElementById('distance');
			var t1 = document.getElementById('trainA');
			var t2 = document.getElementById('trainB');
			var f = document.getElementById('fly');
			var a = document.getElementById('answer');
			var answer = superFly(parseFloat(d.value), parseFloat(t1.value), parseFloat(t2.value), parseFloat(f.value));
			a.innerHTML = answer;
		}