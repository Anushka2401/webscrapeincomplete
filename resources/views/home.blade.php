@extends('master')

@section('title','home')

@section('content')
    <form action= '/create' method='post'>
        <input type="text" name='item' placeholder='enter ur search item'>

@endsection