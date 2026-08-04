package readme_test

import (
	"os"
	"path/filepath"
	"regexp"
	"strings"
	"testing"
)

func TestReadmeGenerateUsesGroupsFlag(t *testing.T) {
	readme, err := os.ReadFile(filepath.Join("..", "README.md"))
	if err != nil {
		t.Fatalf("reading README.md: %v", err)
	}

	re := regexp.MustCompile("(?s)```bash\\n(.*?)\\n```")
	for _, match := range re.FindAllSubmatch(readme, -1) {
		block := string(match[1])
		if !strings.Contains(block, "l8k generate") {
			continue
		}
		for _, line := range strings.Split(block, "\n") {
			if strings.Contains(line, "--group ") && !strings.Contains(line, "--groups ") {
				t.Errorf("README 'l8k generate' example uses --group, expected --groups: %s", strings.TrimSpace(line))
			}
		}
	}
