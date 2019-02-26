import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";

export interface Result {
  resultat: string;
  level: number;
}

@Injectable()

export class TextSummarizeService {
  
  value = "";
  constructor(private http: HttpClient) { }
  getValue() {
    return this.value;
  }
  setValue(value: string, level: number) {

    let httpParams = new HttpParams()
    .set('texte', value).set('level', ""+level);
    this.http.get("http://localhost:5000/", {
      params: httpParams,
    }).subscribe(
      (result: Result) => {
        this.value = result.resultat;
        console.log(result.level+"");
      }
    );
  }
  resume(value: string, level: number) {
    let httpParams = new HttpParams()
    .set('texte', value).set('level', ""+level);
    this.http.get("http://localhost:5000/resume", {
      params: httpParams,
    }).subscribe(
      (result: Result) => {
        this.value = result.resultat;
      }
    );
  }
}
