double clight = TMath::C();
double pi = TMath::Pi();

double AIP1	       = ATAN(sep_ARC/2/Dsep1);
double AIP2	       = ATAN(sep_ARC/2/Dsep2);
double AIP3	       = ATAN((sep_IR3-sep_ARC)/2/Dsep3);
double AIP4	       = ATAN((sep_IR4-sep_ARC)/2/Dsep4);
double AIP5	       = ATAN(sep_ARC/2/Dsep5);
double AIP7	       = ATAN((sep_IR7-sep_ARC)/2/Dsep7);
double AIP8	       = ATAN((sep_ARC)/2/Dsep8);

double AD1__LR1	 := AIP1/6*(1-R0);
double AD2__L1                         := AIP1*(1-R0);
double AD2__R1                         := AIP1*(1-R0);
double l__MBRS              = 9.45;
double AD3__R4                         := AIP4*(1-R0);
