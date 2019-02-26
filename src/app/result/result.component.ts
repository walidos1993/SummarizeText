import { Component, OnInit, SimpleChanges, Input } from '@angular/core';
 import { interval } from 'rxjs';
import { TextSummarizeService } from '../text-summarize.service';
@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements OnInit {
  value: any;
  taille: number;
  constructor(private tsum: TextSummarizeService) { }

  ngOnInit() {
    this.value= this.getValue();
// Create an Observable that will publish a value on an interval
const secondsCounter = interval(1000).subscribe(
      (value) => {
        this.value = this.getValue();
        this.taille= this.getValue().length;
      },
      (error) => {
        console.log('Uh-oh, an error occurred! : ' + error);
      },
      () => {
        console.log('Observable complete!');
      }
    );
  }

  getValue(){return this.tsum.getValue();
  }
}
