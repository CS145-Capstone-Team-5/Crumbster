import { TestBed } from '@angular/core/testing';

import { IonicBackendService } from './ionic-backend.service';

describe('IonicBackendService', () => {
  let service: IonicBackendService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(IonicBackendService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
