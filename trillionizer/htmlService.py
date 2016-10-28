
from __future__ import unicode_literals
from django.http import HttpResponse
import datetime
from characters.models import Character, Rankings

def frontPage(request):
    html = """<html>
<head>
<link href="https://fonts.googleapis.com/css?family=Candal" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,700,900" rel="stylesheet">


<style>
p{
  font-family: 'Roboto', sans-serif;
}
body {
  margin: 0;
  background: #000;
}

.stopfade {
   opacity: .5;
}
.characterName {

  font-family: 'Candal', sans-serif;
    font-weight: 400;
    font-size: 50px;
    opacity: .95;
    position: absolute;
    margin-left:130px;
    left:0px;
    margin-top:18px;
}

table{
    background-color: rgba(255, 255, 255, 0.79) !important;
    border-radius: 10px !important;
}



#polina {
  font-family: Roboto;
  font-weight:100;
  background: rgba(0,0,0,0.3);
  color: white;
  padding: 2rem;
  width: 33%;
  margin:2rem;
  float: right;
  font-size: 20px;
}
h1 {
  font-size: 3rem;
  text-transform: uppercase;
  margin-top: 0;
  letter-spacing: .3rem;
}
#polina button {
  display: block;
  width: 80%;
  padding: .4rem;
  border: none;
  margin: 1rem auto;
  font-size: 1.3rem;
  background: rgba(255,255,255,0.23);
  color: #fff;
  border-radius: 3px;
  cursor: pointer;
  transition: .3s background;
}
#polina button:hover {
   background: rgba(0,0,0,0.5);
}

a {
  display: inline-block;
  color: #fff;
  text-decoration: none;
  background:rgba(0,0,0,0.5);
  padding: .5rem;
  transition: .6s background;
}
a:hover{
  background:rgba(0,0,0,0.9);
}
::-webkit-scrollbar { 
    display: none; 
}
@media screen and (max-width: 500px) {
  div{width:70%;}
}
@media screen and (max-device-width: 800px) {
  html { background: url(//demosthenes.info/assets/images/polina.jpg) #000 no-repeat center center fixed; }
  #bgvid { display: none; }
}
span{
font-family: 'Candal', sans-serif;
font-weight:700;
}
#menu{
margin-top:50px;
}
#menu > span{
margin-top:-10px;
margin-left:100px;
font-size:20px;
}
.table>tbody>tr>td, .table>tbody>tr>th, .table>tfoot>tr>td, .table>tfoot>tr>th, .table>thead>tr>td, .table>thead>tr>th{
  text-align:center;
}
.characterBoxes{
  height:350px;
  border: rgba(27, 27, 27, 0.54) solid 1px;
  background-color: rgba(49, 45, 45, 0.47);
}

}

.Valiant360_default canvas{
  position:fixed !important;
}
canvas{
position:fixed !important;
z-index:1;
}
</style>
</head>
<body>

<!-- required libraries -->
<script src="static/js/jquery-1.7.2.min.js"></script>
<script src="static/js/three.min.js"></script>

<!-- Valiant360 plugin -->
<script src="static/js/jquery.valiant360.min.js"></script>

<!-- Valiant360 styles -->
<link rel="stylesheet" type="text/css" href="static/css/valiant360.css">

<!-- Valiant360 player container -->

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>


<!--
<video poster="https://s3-us-west-2.amazonaws.com/s.cdpn.io/4273/polina.jpg" id="bgvid" playsinline autoplay muted loop>
  <!-- WCAG general accessibility recommendation is that media such as background video play through only once. Loop turned on for the purposes of illustration; if removed, the end of the video will fade in the same way created by pressing the "Pause" button  -->
<!--<source src="http://video.webmfiles.org/big-buck-bunny_trailer.webm" type="video/webm">
<source src="http://thenewcode.com/assets/videos/polina.mp4" type="video/mp4">
</video>
-->
<div class="valiant" data-video-src="static/warcraft.mp4" style="height:100%"></div>
<div id="polina" style="position:absolute;top:0px;height:100px;width:100%;background-color:rgba(49, 49, 49, 0.85);margin:0px;padding:0px;position:fixed;z-index:10;">
<div id="menu">
<img src="static/logo_white.png" style="position:absolute;margin-top:-31px;left:35px;width:117px;">
<span style="margin-left:200px;">WHO WE ARE</span>
<span>RECRUITMENT</span>
<span>ARE WE ONLINE?</span>
</div>
<img src="static/logo_white.png" style="position: fixed;
    left: 50%;
    top: 50%;
    margin-left: -400px;
    width: 800px;
    margin-top: -250px;
    opacity: .6;">
</div>
<div style="height:100%;width:100%;background-color:rgba(255, 0, 0, 0.83);z-index:10;position:absolute;">
<div id="polina" style="margin-top:150px;">
<h1>Trillion</h1>
<p>7/7 Heroic | Area-52
<p><a href="http://www.wowprogress.com/guild/us/Garona/Trillion">WoW-Progress</a>
<p>Over the years, you may find that rare long-lasting friendships can be made. Here at Trillion, we are comprised of players who have spent years and years of gaming experiences together -- spanning across multiple games and ecosystems coming back together to vanquish the Legion throughout Azeroth.</p>
<p>New Guilies and Oldies alike, we find character and personality the most important trait for friends and raiders.</p>
<p>With multiple players with top world-first achievements under the belt, we seek to find the balance between pushing content and maintaining casual gameplay.</p>
</div>
</div>
<div style="height:100%;width:100%;background-color:rgba(0, 0, 255, 0.85);top:200%;position:absolute;z-index:10;">
<center>
<div id="polina" style="width:90%;float:none;margin-top: 170px;">
<div class="container-fluid">
  <div class="row" id="characterBoxes" style="overflow:scroll;max-height:900px;">
    
</div>

  </div>
</div>
</div>
</center>
</div>
<script>
// instantiate script on your container
 $('.valiant').Valiant360({
        crossOrigin: 'anonymous',   // valid keywords: 'anonymous' or 'use-credentials'
        clickAndDrag: true,    // use click-and-drag camera controls
        keyboardControls: true, // use keyboard controls (move by arrows)
        flatProjection: false,  // map image to appear flat (often more distorted)
        fov: 10,                // initial field of view
        fovMin: 3,              // min field of view allowed
        fovMax: 100,            // max field of view allowed
        hideControls: true,    // hide player controls
        lon: 180,                 // initial lon for camera angle
        lat: 0,                 // initial lat for camera angle
        loop: "loop",           // video loops by default
        muted: true,            // video muted by default
        volume: 0.5,            // video volume by default
        autoplay: true          // video autoplays by default
    });

	$(".valiant").bind("wheel mousewheel", function(e) {e.preventDefault()});
</script>
<script src="http://www.wearetrillion.com/service/charactersLoad.js"></script>
</body>
</html>"""

    return HttpResponse(html)

def characterJS(request):
    Characters = Character.objects.all()
    JS = ""
    for character in Characters:
        rankingsForCharacter = Rankings.objects.filter(characterID_id=character.pk).order_by('rankNumber')
        JS += str("""$('#characterBoxes').append('<div class="col-md-4 characterBoxes"><div style="position: absolute;margin-left: 10px;"><img style="border-radius:15px;margin-top: 10px;" src=" """) +  str(character.iconURL) +  str(""" "></div><span class="characterName">""")  + str(character.nickName)  + str("""</span><span style="background-color: #ff2b2b; padding: 3px;font-size: 38px;margin-top:28px;border-radius: 20px;float: right;margin-right: 0px;">""") + str(character.itemLevelEquipped) 
        JS += str("""</span>""")
        JS += str("""<div style="max-height: 250px;overflow: scroll;position: inherit;margin-top: 97px;"><table class="table"><thead><tr><th>Link</th><th>Difficulty:</th><th>Boss</th><th>Percentile</th><th>Rank #</th></tr></thead><tbody>""")
        for ranking in rankingsForCharacter:
            rankPercentage =  float(ranking.rankNumber) * 100 
            rankPercentageFixed = float(rankPercentage) / float(ranking.rankOutOf)
            rankPercentageFixedStep2 = 100 - float(rankPercentageFixed)
            rankRounded = int(round(rankPercentageFixedStep2))
            if ranking.difficulty == 1:
                difficulty = "LFR"
            elif ranking.difficulty == 5:
                difficulty = "Mythic"
            elif ranking.difficulty == 2:
                difficulty = "Heroic"
            elif ranking.difficulty == 3:
                difficulty = "Normal"
            elif ranking.difficulty == 4:
                difficulty = "Heroic"
            else:
                difficulty = "Other"
            JS += str("""<tr><th scope="row"><a href="https://www.warcraftlogs.com/reports/""")  +str(ranking.reportID) + str("""">View</a></th><td>""") + str(difficulty) + str("""</th><td>""") + str(ranking.encounterID) +  str("""</td><td>""") + str(rankRounded) + str("""</td><td>""") + str(ranking.rankNumber)+ str("""</td></tr>""")
        JS += str("""</tbody></table></div>""")
        JS += str("""');""")
    return HttpResponse(JS)




