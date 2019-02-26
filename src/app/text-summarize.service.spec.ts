import { TestBed } from '@angular/core/testing';

import { TextSummarizeService } from './text-summarize.service';

describe('TextSummarizeService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TextSummarizeService = TestBed.get(TextSummarizeService);
    expect(service).toBeTruthy();
  });
});
