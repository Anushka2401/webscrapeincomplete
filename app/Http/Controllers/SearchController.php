<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SearchController extends Controller
{
    public function transfer(Request $request){
        $request -> input('item');
        $result = shell_exec("python " . app_path(). "C:\Users\Alisha\scraper_web\public\scraper_code.py" . escapeshellarg($request));
        @foreach($d in $result):
            {{$d}}

    }
}
