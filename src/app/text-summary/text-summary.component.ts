import { Component, OnInit } from '@angular/core';

import { TextSummarizeService } from '../text-summarize.service';
import { Observable, interval } from 'rxjs';
@Component({
  selector: 'app-text',
  templateUrl: './text-summary.component.html',
  styleUrls: ['./text-summary.component.css']
})

export class TextSummaryComponent implements OnInit {
  valeur: string = "walid";
  level: number= 0;
  levelresume: number= 0;
  taille: number = 0;
  constructor(private tSummarize: TextSummarizeService) { }

  ngOnInit() {
    this.tSummarize.setValue(this.valeur, this.level);
  }
  validate(valeur: string) {
    this.taille= valeur.length;
    this.tSummarize.setValue(this.valeur, this.level);
  }
  resume(valeur: string) {
    this.taille= valeur.length;
    this.tSummarize.resume(this.valeur, this.level);
  }

  resum(valeur: string) {

    this.valeur = this.tSummarize.getValue();
    this.level= this.level+1;

  }
}
