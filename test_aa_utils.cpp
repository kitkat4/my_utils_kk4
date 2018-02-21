

void progBarNh(const double progress, const bool first_call);

int main(){

    for(int i = 0; i < 101; i++){
        for(int j = 0; j < 50000000; j++){
            // do nothing
        }
        if(i == 0){
            progBarNh(0.01 * i, true);
        }else{
            progBarNh(0.01 * i, false);
        }
    }
}    
