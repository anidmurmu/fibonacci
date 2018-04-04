from django.shortcuts import render, get_object_or_404
from .models import Album, Song
from django.utils import timezone

def index( request ):
	all_albums = Album.objects.all()
	context = {
		'all_albums' : all_albums
	}
	return render( request, 'music/index.html', context )

def nth_fibonacci( request ):
	number = request.POST.get( 'number' )
	start_time = timezone.now()
	start_time = '{:%S}.{:03d}'.format(start_time, start_time.microsecond // 1000)
	#term = int( request.POST['num'] )
	term = request.POST.get( 'num' )
	term = str( term ).strip()
	term = int( term )
	nth_term = get_fibonacci( term  )
	end_time = timezone.now()
	end_time = '{:%S}.{:03d}'.format(end_time, end_time.microsecond // 1000)
	time = time_diff( start_time, end_time )
	return render( request, 'music/fib.html', {'nth_term':  nth_term, 'time': time } )

def get_fibonacci( term ):
	first_num = 1
	second_num = 1
	if term in ( '1', '2' ):
		return first_num
	count = 3 
	third_num = 0;
	while ( count <= term ):
		third_num = first_num + second_num
		first_num = second_num
		second_num = third_num
		count += 1
	return third_num

def time_diff( start_time, end_time ):
	st_time_milli = start_time.split( "." )
	end_time_milli = end_time.split( "." )
	st_total_milli = int( st_time_milli[0] ) * 1000  + int( st_time_milli[1] )
	end_total_milli =int( end_time_milli[0] )  * 1000 + int( end_time_milli[1] )
	time_differ = end_total_milli - st_total_milli
	second = time_differ / 1000
	milli = ( time_differ % 1000 )
	result = str( second ) + ':' + str( milli ) + "sec"
	return result
		

