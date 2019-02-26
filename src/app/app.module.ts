import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TextSummaryComponent } from './text-summary/text-summary.component';
import { ResultComponent } from './result/result.component';
import { MainComponent } from './main/main.component';
import { TextSummarizeService } from './text-summarize.service';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    TextSummaryComponent,
    ResultComponent,
    MainComponent,
   
    
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,FormsModule
  ],
  
  providers: [TextSummarizeService],
  
  bootstrap: [AppComponent]
})
export class AppModule { }
