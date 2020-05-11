#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int getLine(FILE *fp, char buffer[]) {


	int c = 0;
	int i = 0;
	c = fgetc(fp);
	while(c != EOF && c != '\n') {
		if (c != '\r') {
			buffer[i++] = (char) c;
		}
		c = fgetc(fp);
	}

	buffer[i] = '\0';
	return i;
}

int main(int argc, char *argv[]) {


	char buffer[100] = "";
	FILE *fp;
	fp = fopen(argv[1], "r");
	FILE *fp2 = fopen("output.txt", "w");
	int i = 0;
	while (getLine(fp, buffer) > 0) {

		fprintf(fp2, "\"%s\", ", buffer);
		if (i == 6) {
			fprintf(fp2, "\n");
			i = 0;
		}
		else {
			i++;
		}
	}

	fclose(fp);
	fclose(fp2);
	return 0;

}
