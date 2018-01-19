<?php
$master_course_array=[];
$primo_url='https://alliance-primo.hosted.exlibrisgroup.com/primo-explore/search?query=any,contains,';
$primo_scope='&tab=default_tab&search_scope=lanecc_cr&vid=LANECC&offset=0';

function processfile($filename){
	$course_array=[];
	$jsondata=json_decode(file_get_contents($filename),TRUE);
	$course_array[]=$jsondata['course'];
	#print_r ($courseArray);
	
	foreach ($course_array[0] as $key => $course){
	//echo $course['name'].'<br />'; 
	$course_name_array[]=$course['name'];
	}
	//print_r ($course_name_array);
	return $course_name_array;
}

$course_name_array1=processfile('crjson0'); //files created via Python script
$course_name_array2=processfile('crjson100');
$course_name_array3=processfile('crjson200');
$course_name_array4=processfile('crjson300');

$master_course_array=array_merge($course_name_array1,$course_name_array2,$course_name_array3,$course_name_array4);
//print_r ($master_course_array);

$master_course_array=array_unique($master_course_array); #remove duplicate course names
foreach ($master_course_array as $value){
	echo '<p><a href="'.$primo_url.$value.$primo_scope.'"</a>'.$value.'</p>';
}
?>